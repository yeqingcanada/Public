from django.dispatch import Signal

order_created = Signal()


"""在handler.py中的的方法叫 signal handler,最好将signal和handlers分开。
__init__ is where we define our signals.
signal is simply an instance of the signal class.
order_created = Signal()这句结束,我们就需要fire our signal了。我们需要去到serializer CreateOrderSerializer处fire"""