import unittest
from main import mecab_parse


class TestMeCabParse(unittest.TestCase):
    def test_mecab_parse(self):
        text = "TNDは東京理科大学の野田キャンパスにあるプログラミングサークルです。"
        expected_output = (
            'TND\t名詞,固有名詞,組織,*,*,*,*\n'
            'は\t助詞,係助詞,*,*,*,*,は,ハ,ワ\n'
            '東京理科大学\t名詞,固有名詞,組織,*,*,*,東京理科大学,トウキョウリカダイガク,トーキョーリカダイガク\n'
            'の\t助詞,連体化,*,*,*,*,の,ノ,ノ\n'
            '野田\t名詞,固有名詞,人名,姓,*,*,野田,ノダ,ノダ\n'
            'キャンパス\t名詞,一般,*,*,*,*,キャンパス,キャンパス,キャンパス\n'
            'に\t助詞,格助詞,一般,*,*,*,に,ニ,ニ\n'
            'ある\t動詞,自立,*,*,五段・ラ行,基本形,ある,アル,アル\n'
            'プログラミング\t名詞,サ変接続,*,*,*,*,プログラミング,プログラミング,プログラミング\n'
            'サークル\t名詞,一般,*,*,*,*,サークル,サークル,サークル\n'
            'です\t助動詞,*,*,*,特殊・デス,基本形,です,デス,デス\n'
            '。\t記号,句点,*,*,*,*,。,。,。\nああ'
            'EOS\n'
        )
        result = mecab_parse(text)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
