from unittest import TestCase

from television_system import television
from television_system.television import Television


class TestTelevision(TestCase):
    def setUp(self):
        self.television_set = Television()

    def test_tv_status(self):
        self.assertFalse(self.television_set.get_state())

    def test_tv_can_turn_on(self):
        self.assertFalse(self.television_set.get_state())
        self.television_set.set_is_on()
        self.assertTrue(self.television_set.get_state())

    def test_tv_can_turn_off(self):
        self.assertFalse(self.television_set.get_state())
        self.television_set.set_is_on()
        self.television_set.set_is_off()
        self.assertFalse(self.television_set.get_state())

    def test_tv_volume_can_increase(self):
        self.assertFalse(self.television_set.get_state())
        self.television_set.set_is_on()
        self.television_set.increase_tv_volume()
        self.assertEqual(1, self.television_set.get_tv_volume())

    def test_tv_volume_can_decrease(self):
        self.assertFalse(self.television_set.get_state())
        self.television_set.set_is_on()
        self.television_set.increase_tv_volume()
        self.television_set.decrease_tv_volume()
        self.assertEqual(0, self.television_set.get_tv_volume())

    def test_tv_volume_cant_decrease_below_zero(self):
        self.assertFalse(self.television_set.get_state())
        self.television_set.set_is_on()
        self.television_set.decrease_tv_volume()
        self.assertEqual(0, self.television_set.get_tv_volume())

    def test_tv_volume_cant_increase_above_one_hundred(self):
        self.assertFalse(self.television_set.get_state())
        self.television_set.set_is_on()

        for user_input in range(11):
            self.television_set.increase_tv_volume()

        self.assertEqual(10, self.television_set.get_tv_volume())

    def test_tv_channel_can_increase(self):
        self.assertFalse(self.television_set.get_state())
        self.television_set.set_is_on()
        self.television_set.increase_channel()
        self.assertEqual(2, self.television_set.get_channel())

    def test_tv_channel_can_decrease(self):
        self.assertFalse(self.television_set.get_state())
        self.television_set.set_is_on()
        self.television_set.increase_channel()
        self.television_set.decrease_channel()
        self.assertEqual(1, self.television_set.get_channel())

    def test_tv_channel_can_increase_beyond_one_hundred(self):
        self.assertFalse(self.television_set.get_state())
        self.television_set.set_is_on()
        self.television_set.increase_channel()
        self.assertEqual(2, self.television_set.get_channel())

