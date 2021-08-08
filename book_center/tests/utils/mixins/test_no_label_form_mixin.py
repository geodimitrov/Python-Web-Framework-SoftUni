from book_center.utils.mixins import NoLabelFormMixin
from django.test import TestCase, RequestFactory
from django.views.generic import TemplateView


class NoLabelFormMixinTest(TestCase):

    class DummyView(NoLabelFormMixin, TemplateView):
        pass

    def setUp(self):
        super(NoLabelFormMixinTest, self).setUp()
        self.request = RequestFactory().get('/fake-path')
        self.view = self.DummyView()

    def test_context_data_no_args(self):
        boostrap = self.view._init_bootstrap()
        self.assertEqual(boostrap['label'], '')