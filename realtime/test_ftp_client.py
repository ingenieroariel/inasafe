"""
InaSAFE Disaster risk assessment tool developed by AusAid and World Bank
- **Ftp Client Test Cases.**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'tim@linfiniti.com'
__version__ = '0.5.0'
__date__ = '19/07/2012'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

import unittest
from realtime.ftp_client import FtpClient
from realtime.realtime import DATA_DIR


class FtpClientTest(unittest.TestCase):
    """Test the ftp client used to fetch shake listings"""
    _expectedFiles = ('20110413170148.inp.zip'
                   '20110413170148.out.zip')


    def test_getDirectoryListingUsingUrlLib2(self):
        """Check if we can get a nice directory listing using urllib2"""
        myClient = FtpClient()
        myListing = myClient.getListing()
        myMessage = ('Expected this list:\n%s\nTo contain these items:\n%s' %
                      myListing, _expectedFiles)
        assert myExpectedFiles in myListing, myMessage

    def test_getDirectoryListingUsingFtpLib(self):
        """Check if we can get a nice directory listing using ftplib"""
        myClient = FtpClient(theBackend='ftplib')
        myListing = myClient.getListing()
        myMessage = ('Expected this list:\n%s\nTo contain these items:\n%s' %
                      myListing, _expectedFiles)
        assert myExpectedFiles in myListing, myMessage

    def test_getShakeMapInput(self):
        """Check that we can retrieve a shakemap 'inp' input file"""
        myShakeEvent = '20110413170148'
        myClient = FtpClient()
        myShakemapFile =  myClient.fetchInput(myShakeEvent)
        myExpectedFile = os.path.join(DATA_DIR, myShakeEvent + 'inp.zip')
        myMessage = 'Expected path for downloaded shakemap not received'
        self.assertEqual(myShakemapFile, myExpectedFile, myMessage)

    def test_getShakeMapOutput(self):
        """Check that we can retrieve a shakemap 'out' input file"""
        myShakeEvent = '20110413170148'
        myClient = FtpClient()
        myShakemapFile =  myClient.fetchOutput(myShakeEvent)
        myExpectedFile = os.path.join(DATA_DIR, myShakeEvent + 'out.zip')
        myMessage = 'Expected path for downloaded shakemap not received'
        self.assertEqual(myShakemapFile, myExpectedFile, myMessage)

    def test_getShakeMap(self):
        """Check that we can retrieve both input and output from ftp at once"""
        myShakeEvent = '20110413170148'
        myClient = FtpClient()
        myInpFile, myOutFile =  myClient.fetch(myShakeEvent)
        myExpectedInpFile = os.path.join(DATA_DIR, myShakeEvent + 'inp.zip')
        myExpectedOutFile = os.path.join(DATA_DIR, myShakeEvent + 'out.zip')
        myMessage = 'Expected path for downloaded shakemap INP not received'
        self.assertEqual(myInpFile, myExpectedInpFile, myMessage)
        myMessage = 'Expected path for downloaded shakemap OUT not received'
        self.assertEqual(myOutFile, myExpectedOutFile, myMessage)




if __name__ == '__main__':
    suite = unittest.makeSuite(FtpClientTest, 'test')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)