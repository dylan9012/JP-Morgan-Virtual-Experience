import unittest

from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            bid_price = quote['top_ask']['price']
            ask_price = quote['top_bid']['price']
            self.assertEqual(getDataPoint(quote)[3], (bid_price + ask_price) / 2)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            bid_price = quote['top_ask']['price']
            ask_price = quote['top_bid']['price']
            self.assertEqual(getDataPoint(quote)[3], (bid_price + ask_price) / 2)

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_calculateRatio_ratioGreaterThanOne(self):
        quotes = [
            {'top_ask': {'price': 200.42, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 300.12, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        price_a = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
        price_b = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
        self.assertGreater(getRatio(price_a, price_b), 1)

    def test_getRatio_calculateRatio_ratioLessThanOne(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 200.42, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 300.12, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        price_a = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
        price_b = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
        self.assertLess(getRatio(price_a, price_b), 1)

    def test_getRatio_calculateRatio_ratioEqualsOne(self):
        quotes = [
            {'top_ask': {'price': 100.01, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 100.01, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 100.01, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 100.01, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        price_a = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
        price_b = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
        self.assertEqual(getRatio(price_a, price_b), 1)

    def test_getRatio_calculateRatio_priceAEqualsZero(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        price_a = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
        price_b = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
        self.assertEqual(getRatio(price_a, price_b), 0)

    def test_getRatio_calculateRatio_priceBEqualsZero(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        price_a = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
        price_b = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
        self.assertIsNone(getRatio(price_a, price_b))

if __name__ == '__main__':
    unittest.main()
