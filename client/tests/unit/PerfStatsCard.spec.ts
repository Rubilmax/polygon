import { shallowMount } from '@vue/test-utils';
import PerfStatsCard from '@/pages/Home/components/PerfStatsCard/PerfStatsCard.vue';

describe('PerfStatsCard.vue', () => {
  it('should match snapshot', () => {
    expect(
      shallowMount(PerfStatsCard, {
        propsData: { title: 'Le Seigneur Des Anneaux', timeframeHours: '9' },
      }),
    ).toMatchSnapshot();
  });
});
