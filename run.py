from quote_engine import Ingestor


quote = Ingestor.parse('./_data/SimpleLines/SimpleLines.pdf')
quote += Ingestor.parse('./_data/SimpleLines/SimpleLines.txt')
quote += Ingestor.parse('./_data/SimpleLines/SimpleLines.csv')
quote += Ingestor.parse('./_data/SimpleLines/SimpleLines.docx')
for num, quote in enumerate(quote):
    print(num, quote)
