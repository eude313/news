import unittest
from app.models import Articles

class test_articles(unittest.TestCase):
    '''
      Test Class to test the behaviour of the Articles class
      '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article= Articles("2021-08-10T04:01:00Z",' "https://cdn.vox-cdn.com/thumbor/f0vyQU4yPS3Q_YkajmFrSOnqpKs=/0x133:3768x2106/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22772464/1_Windows_on_Macbook_Pro_Parallels_Desktop_17_for_Mac.png','A thrilling new article','content','Awadh',' "https://www.theverge.com/2021/8/10/22617544/parallels-17-mac-windows-11-preview-emulation-performance-upgrades')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_article, Articles))