# -*- coding: utf-8 -*-
# ***********************************************************************
# ******************  CANADIAN ASTRONOMY DATA CENTRE  *******************
# *************  CENTRE CANADIEN DE DONNÉES ASTRONOMIQUES  **************
#
#  (c) 2018.                            (c) 2018.
#  Government of Canada                 Gouvernement du Canada
#  National Research Council            Conseil national de recherches
#  Ottawa, Canada, K1A 0R6              Ottawa, Canada, K1A 0R6
#  All rights reserved                  Tous droits réservés
#
#  NRC disclaims any warranties,        Le CNRC dénie toute garantie
#  expressed, implied, or               énoncée, implicite ou légale,
#  statutory, of any kind with          de quelque nature que ce
#  respect to the software,             soit, concernant le logiciel,
#  including without limitation         y compris sans restriction
#  any warranty of merchantability      toute garantie de valeur
#  or fitness for a particular          marchande ou de pertinence
#  purpose. NRC shall not be            pour un usage particulier.
#  liable in any event for any          Le CNRC ne pourra en aucun cas
#  damages, whether direct or           être tenu responsable de tout
#  indirect, special or general,        dommage, direct ou indirect,
#  consequential or incidental,         particulier ou général,
#  arising from the use of the          accessoire ou fortuit, résultant
#  software.  Neither the name          de l'utilisation du logiciel. Ni
#  of the National Research             le nom du Conseil National de
#  Council of Canada nor the            Recherches du Canada ni les noms
#  names of its contributors may        de ses  participants ne peuvent
#  be used to endorse or promote        être utilisés pour approuver ou
#  products derived from this           promouvoir les produits dérivés
#  software without specific prior      de ce logiciel sans autorisation
#  written permission.                  préalable et particulière
#                                       par écrit.
#
#  This file is part of the             Ce fichier fait partie du projet
#  OpenCADC project.                    OpenCADC.
#
#  OpenCADC is free software:           OpenCADC est un logiciel libre ;
#  you can redistribute it and/or       vous pouvez le redistribuer ou le
#  modify it under the terms of         modifier suivant les termes de
#  the GNU Affero General Public        la “GNU Affero General Public
#  License as published by the          License” telle que publiée
#  Free Software Foundation,            par la Free Software Foundation
#  either version 3 of the              : soit la version 3 de cette
#  License, or (at your option)         licence, soit (à votre gré)
#  any later version.                   toute version ultérieure.
#
#  OpenCADC is distributed in the       OpenCADC est distribué
#  hope that it will be useful,         dans l’espoir qu’il vous
#  but WITHOUT ANY WARRANTY;            sera utile, mais SANS AUCUNE
#  without even the implied             GARANTIE : sans même la garantie
#  warranty of MERCHANTABILITY          implicite de COMMERCIALISABILITÉ
#  or FITNESS FOR A PARTICULAR          ni d’ADÉQUATION À UN OBJECTIF
#  PURPOSE.  See the GNU Affero         PARTICULIER. Consultez la Licence
#  General Public License for           Générale Publique GNU Affero
#  more details.                        pour plus de détails.
#
#  You should have received             Vous devriez avoir reçu une
#  a copy of the GNU Affero             copie de la Licence Générale
#  General Public License along         Publique GNU Affero avec
#  with OpenCADC.  If not, see          OpenCADC ; si ce n’est
#  <http://www.gnu.org/licenses/>.      pas le cas, consultez :
#                                       <http://www.gnu.org/licenses/>.
#
#  $Revision: 4 $
#
# ***********************************************************************
#

import os

from caom2pipe import manage_composable as mc
from draost2caom2 import draost_name

TEST_FILES_DIR = '/test_files'

def test_storage_name():
    d_name1 = 'DRAO_ST_CGPS_RN43_20180715T1450_C21.tar.gz'
    d_name2 = 'DRAO_ST_CGPS_RN43_20180715T1450_C74.tar.gz'
    d_name3 = 'DRAO_ST_CGPS_RN43_20180715T1450_RAW.tar.gz'
    d_name4 = 'DRAO_ST_CGPS_RN43_20180715T1450_S21.tar.gz'
    test_f_names = sorted([d_name1, d_name2, d_name3,
                           d_name4])
    f_name = 'RN43.json'
    test_subject = draost_name.DraoSTName(fname_on_disk=f_name)
    assert test_subject.is_valid(), 'should be valid'
    assert test_subject.obs_id == 'RN43', 'wrong obs_id'
    assert test_subject.product_id is None, 'not maintained by pipeline'
    assert test_subject.file_uri is None, 'not maintained by pipeline'
    assert test_subject.lineage is None, 'not maintained by pipeline'
    test_config = mc.Config()
    test_config.get_executors()
    test_config.working_directory = TEST_FILES_DIR
    for ii in test_f_names:
        f_name = f'{TEST_FILES_DIR}/{ii}'
        if not os.path.exists(f_name):
            with open(f_name, 'w') as f:
                f.write('test content')

    test_result = draost_name.DraoSTName.get_f_names(
        test_subject.obs_id, test_config.working_directory)
    assert test_result == test_f_names, \
        'two ways to name'
