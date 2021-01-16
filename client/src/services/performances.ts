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
