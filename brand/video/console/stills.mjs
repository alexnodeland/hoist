// The console's screenshots for the README and the guide (brand/media/console/):
// the overview, a server, a served session, a flow and an audit job, each in
// the light and the dark theme, 1440 x 900, from the real hoist-console that
// capture.sh serves over the test fixtures. capture.mjs runs first and leaves
// shots/shots.json, whose session and job addresses this reads, so it needs no
// id of its own. The pictures are then reduced to 256 colors by
// brand/tools/quantize_stills.py.
//
//   node video/console/stills.mjs [--url http://127.0.0.1:7891]
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launchBrowser, option } from '../lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const URL0 = option(process.argv.slice(2), '--url', 'http://127.0.0.1:7891');
const out = path.join(here, '..', '..', 'media', 'console');
fs.mkdirSync(out, { recursive: true });

// The addresses capture.mjs shot, as the film shows them (127.0.0.1:7878/...).
const shots = JSON.parse(fs.readFileSync(path.join(here, 'shots', 'shots.json'), 'utf8')).shots;
const pathOf = id => {
  const s = shots.find(x => x.id === id);
  if (!s) throw new Error(`stills: capture.mjs left no shot "${id}"`);
  return s.url.replace(/^127\.0\.0\.1:7878/, '') || '/';
};

const pages = [
  { name: 'overview', url: '/' },
  {
    name: 'server',
    url: '/servers/shop',
    act: async page => {
      await page.getByTestId('probe').click();
      await page.getByTestId('probe-ok').waitFor({ timeout: 30_000 });
    },
  },
  { name: 'session', url: pathOf('session') },
  { name: 'flow', url: '/flows/shop' },
  { name: 'jobs', url: pathOf('job') },
];

const browser = await launchBrowser();
for (const theme of ['light', 'dark']) {
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, colorScheme: theme, reducedMotion: 'reduce' });
  await context.addInitScript(t => {
    try {
      localStorage.setItem('hoist-console:theme', t);
      localStorage.removeItem('hoist-console:domain');
    } catch {}
  }, theme);
  const page = await context.newPage();
  page.on('pageerror', e => { console.error(e); process.exitCode = 1; });
  for (const p of pages) {
    await page.goto(URL0 + p.url, { waitUntil: 'load' });
    await page.locator('h1').first().waitFor();
    await page.waitForTimeout(700);
    if (p.act) await p.act(page);
    await page.mouse.move(1439, 899); // no hover state in the picture
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(out, `${p.name}-${theme}.png`) });
    console.log(`stills: ${p.name}-${theme} ${p.url}`);
  }
  await context.close();
}
await browser.close();
