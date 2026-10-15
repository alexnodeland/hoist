<template>
  <kbd class="kbd"><slot /></kbd>
</template>

<style scoped>
.kbd {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 20px;
  height: 20px;
  padding: 0 5px;
  border-radius: 5px;
  border: 1px solid var(--hoist-border);
  border-bottom-width: 2px;
  background: var(--hoist-surface);
  color: var(--hoist-text-subtle);
  font-family: var(--hoist-font-sans);
  font-size: 11px;
  font-weight: 500;
  line-height: 1;
}
</style>
