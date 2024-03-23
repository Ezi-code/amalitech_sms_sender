from django.test import TestCase
from .models import Messages, Templates, MessageHistory

class MessagesTestCase(TestCase):
    def setUp(self):
        Messages.objects.create(content="This is a test message", receipients="08012345678, 08012345679", draft=False)
        Messages.objects.create(content="This is a test message", receipients="08012345678, 08012345679", draft=True)

    def test_messages_draft(self):
        message = Messages.objects.get(draft=False)
        self.assertEqual(message.draft, False)
        message = Messages.objects.get(draft=True)
        self.assertEqual(message.draft, True)

    def test_messages_receipients(self):
        message = Messages.objects.get(draft=True)
        self.assertEqual(message.receipients, "08012345678, 08012345679")


