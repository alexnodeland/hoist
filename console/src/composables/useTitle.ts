/** The document's title: "<page> · Hoist console". */
import { watchEffect } from 'vue'

export function useTitle(title: () => string | null | undefined): void {
  watchEffect(() => {
    const t = title()
    document.title = t ? `${t} · Hoist console` : 'Hoist console'
  })
}
