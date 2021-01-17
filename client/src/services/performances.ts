import superagent from 'superagent';

import { BASE_URL } from './networking';

export interface Performances {
  minCompletionTime: number;
  avgCompletionTime: number;
  maxCompletionTime: number;
}

export const getPerformances = async (timeframeHours: number): Promise<Performances> => {
  const { body: PerformancesResponse } = await superagent.get(`${BASE_URL}/performances`).query({ timeframeHours });

  return PerformancesResponse;
};

export const getTimeDisplay = (time: number) => {
  if (time < 0) return 'Unknown';

  if (time >= 1) {
    return Math.round(time * 100) / 100 + 's';
  }

  return Math.round(time * 1000 * 100) / 100 + 'ms';
};
