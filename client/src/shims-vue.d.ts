declare module '*.vue' {
  import Vue from 'vue';
  export default Vue;
}

declare interface PerfStats {
  minCompletionTime: number;
  avgCompletionTime: number;
  maxCompletionTime: number;
}
