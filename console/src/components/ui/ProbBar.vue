<script setup lang="ts">
/**
 * A decision's value against the threshold: a small meter filled to the
 * value, with a tick at the threshold. Petrol when the flow acts on it; the
 * words beside it say the same, so the color is never the only cue.
 */
import { computed } from 'vue'
import { formatProb } from '@/lib/format'

const props = withDefaults(
  defineProps<{
    value: number | null
    threshold: number
    acts: boolean
    width?: number
    showText?: boolean
  }>(),
  { width: 96, showText: true },
)
const percent = (x: number) => Math.round(Math.max(0, Math.min(1, x)) * 10000) / 100
const pct = computed(() => percent(props.value ?? 0))
const tick = computed(() => percent(props.threshold))
const relation = computed(() =>
  props.value === null ? '' : props.value >= props.threshold ? '≥' : '<',
)
</script>

<template>
  <span class="pb">
    <span
      class="pb-track"
      :style="{ width: `${width}px` }"
      role="meter"
      :aria-valuenow="value ?? undefined"
      aria-valuemin="0"
      aria-valuemax="1"
      :aria-label="`${formatProb(value)} against a threshold of ${formatProb(threshold)}`"
    >
      <span class="pb-fill" :class="{ acts }" :style="{ width: `${pct}%` }" />
      <span class="pb-tick" :style="{ left: `${tick}%` }" />
    </span>
    <span v-if="showText" class="pb-text num">
      <strong>{{ formatProb(value) }}</strong>
      <span class="pb-rel">{{ relation }} {{ formatProb(threshold) }}</span>
    </span>
  </span>
</template>

<style scoped>
.pb {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  white-space: nowrap;
}

.pb-track {
  position: relative;
  flex: none;
  height: 8px;
  border-radius: 4px;
  background: var(--hoist-surface-2);
  box-shadow: inset 0 0 0 1px var(--hoist-border);
}

.pb-fill {
  position: absolute;
  inset: 0 auto 0 0;
  border-radius: 4px;
  background: var(--hoist-chart-baseline);
}

.pb-fill.acts {
  background: var(--hoist-chart-accent);
}

.pb-tick {
  position: absolute;
  top: -3px;
  bottom: -3px;
  width: 2px;
  margin-left: -1px;
  border-radius: 1px;
  background: var(--hoist-text);
}

.pb-text {
  font-size: 12.5px;
  color: var(--hoist-text-muted);
}

.pb-text strong {
  font-weight: 600;
  color: var(--hoist-text);
}

.pb-rel {
  margin-left: 4px;
  color: var(--hoist-text-subtle);
}
</style>
