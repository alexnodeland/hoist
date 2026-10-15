// Copies the paper's PDF (paper/latex/hoist.pdf, which `make` there builds
// from the Markdown) into public/, so that the site serves it at
// paper/hoist.pdf, in development and in the build. The copy is ignored by
// git: paper/latex/ stays the only source.
import { copyFileSync, existsSync, mkdirSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

const from = fileURLToPath(new URL('../../paper/latex/hoist.pdf', import.meta.url))
const dir = fileURLToPath(new URL('../public/paper/', import.meta.url))
if (!existsSync(from)) {
  console.error('paper/latex/hoist.pdf is missing: run make in paper/latex')
  process.exit(1)
}
mkdirSync(dir, { recursive: true })
copyFileSync(from, `${dir}hoist.pdf`)
console.log('Copied the paper’s PDF into website/public/paper/')
