import { shallowMount } from '@vue/test-utils';
import AppBar from '@/components/AppBar/AppBar.vue';

describe('AppBar.vue', () => {
  it('should match snapshot', () => {
    expect(shallowMount(AppBar)).toMatchSnapshot();
  });
});
