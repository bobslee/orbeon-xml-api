from .test_common import CommonTestCase
from builder import Bind
from controls import Control


class BuilderTestCase(CommonTestCase):

    def test_set_binds(self):
        for name, bind in self.builder.binds.items():
            self.assertIn(name, self.bind_names)
            self.assertIsInstance(bind, Bind)

    def test_set_controls(self):
        for name, control in self.builder.controls.items():
            self.assertIn(name, self.control_names)
            self.assertIsInstance(control, Control)
