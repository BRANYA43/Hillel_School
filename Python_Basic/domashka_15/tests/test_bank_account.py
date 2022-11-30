import unittest
from tasks.bank_account import BankAccount, Transaction, Decimal


class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.bank_acc = BankAccount('Bogdan')

    def test_deposit(self):
        self.bank_acc.deposit('100')
        self.assertEqual(Decimal('99.00'), self.bank_acc.balance)
        self.assertNotEqual(0, len(self.bank_acc.transactions))
        self.assertEqual(Decimal('1'), self.bank_acc.transactions[0].commission_calculated)

    def test_withdrawal(self):
        self.bank_acc.deposit('1000')
        self.bank_acc.withdrawal('100')
        self.assertNotEqual(0, len(self.bank_acc.transactions))
        self.assertEqual(Decimal('889.00'), self.bank_acc.balance)
        self.assertEqual(Decimal('1'), self.bank_acc.transactions[-1].commission_calculated)
        self.bank_acc.withdrawal('1000')
        self.assertEqual(Decimal('889.00'))
        self.assertEqual('Failed', self.bank_acc.transactions[-1].status)