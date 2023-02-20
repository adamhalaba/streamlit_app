import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px

#Unique values of columns
unique_is_new_user = [1, 0]
unique_id_charter_company = [16, 131, 297, 1371, 1059, 223, 1376, 524, 402, 80, 518, 190, 1310, 463, 441, 967, 164, 791, 300, 1005, 1012, 1043, 953, 1073, 457, 77, 671, 639, 1263, 231, 1015, 192, 1031, 108, 85, 236, 1430, 182, 127, 1453, 922, 22, 1444, 1013, 530, 1289, 54, 948, 1370, 240, 165, 1345, 116, 355, 720, 130, 30, 1195, 1393, 513, 545, 89, 213, 1112, 1316, 186, 535, 225, 1245, 1378, 1075, 1326, 1159, 833, 997, 1074, 974, 13, 1297, 175, 1243, 476, 985, 12, 19, 807, 1208, 934, 426, 1194, 1034, 1356, 1003, 532, 202, 389, 1002, 166, 37, 776, 1260, 909, 1384, 877, 154, 1336, 1341, 827, 921, 578, 1064, 491, 1339, 140, 509, 1320, 647, 465, 958, 1126, 46, 168, 69, 1279, 493, 1145, 736, 1175, 20, 1166, 15, 176, 277, 405, 600, 1061, 935, 217, 730, 609, 558, 1097, 1470, 1390, 1142, 78, 1421, 675, 199, 871, 205, 1226, 371, 1298, 623, 1082, 751, 351, 425, 1113, 105, 372, 466, 916, 1267, 1469, 189, 1110, 703, 626, 1275, 172, 769, 1412, 724, 39, 1223, 814, 242, 427, 872, 1445, 230, 1457, 304, 1353, 197, 1454, 207, 677, 1203, 661, 32, 265, 1334, 1388, 828, 940, 1154, 390, 349, 1150, 603, 1387, 1418, 960, 1427, 595, 296, 738, 1405, 1294, 145, 178, 566, 229, 43, 1007, 138, 973, 170, 281, 309, 568, 144, 1070, 386, 824, 890, 742, 737, 31, 680, 48, 1343, 282, 995, 28, 613, 901, 1250, 1448, 1340, 408, 500, 273, 552, 770, 966, 95, 451, 279, 1415, 1270, 782, 1101, 1282, 1337, 1222, 823, 932, 5, 655, 1139, 295, 71, 593, 1322, 347, 1253, 429, 139, 1104, 298, 1072, 1333, 267, 622, 999, 634, 673, 630, 617, 337, 931, 221, 150, 370, 804, 905, 670, 1306, 283, 467, 1205, 1406, 1050, 1404, 712, 1006, 260, 1212, 1291, 1347, 1036, 637, 292, 757, 1414, 950, 385, 68, 1256, 548, 82, 368, 1186, 1189, 1182, 915, 1062, 132, 1484, 24, 914, 1439, 1450, 237, 49, 912, 1228, 955, 1435, 1302, 377, 874, 163, 413, 330, 44, 51, 470, 450, 886, 52, 1438, 100, 216, 1052, 1071, 906, 1144, 1240, 72, 314, 584, 880, 933, 939, 943, 1368, 162, 1359, 1349, 313, 1216, 1462, 911, 1319, 1128, 73, 642, 842, 582, 1100, 1458, 1106, 981, 763, 1261, 883, 41, 1206, 1185, 725, 689, 1451, 1111, 726, 984, 119, 431, 322, 1028, 112, 1498, 840, 1176, 1425, 60, 1077, 359, 1329, 1168, 1014, 926, 1063, 1464, 529, 479, 248, 1183, 320, 579, 1118, 1278, 536, 1023, 1069, 311, 574, 1035, 261, 196, 631, 1436, 1011, 519, 1257, 128, 708, 1044, 1342, 560, 53, 1315, 437, 977, 946, 1123, 816, 1409, 1201, 1325, 907, 570, 384, 1153, 1395, 1332, 222, 1090, 957, 238, 1268, 21, 910, 885, 444, 1089, 1038, 1096, 6, 1363, 1127, 1443, 226, 123, 1447, 1284, 1274, 1239, 452, 1407, 1105, 672, 1255, 1247, 74, 1076, 210, 573, 1377, 698, 903, 1053, 1192, 1254, 972, 383, 1281, 181, 141, 1379, 835, 944, 382, 608, 1502, 554, 1138, 325, 1308, 1236, 2, 1493, 1202, 1054, 787, 1079, 407, 1042, 993, 198, 1283, 84, 1171, 620, 1129, 956, 1301, 1152, 7, 50, 87, 1288, 1433, 1372, 746, 605, 881, 275, 669, 433, 245, 616, 889, 1494, 376, 1452, 1499, 113, 1033, 656, 496, 1098, 754, 862, 502, 380, 812, 919, 1386, 1423, 1102, 448, 658, 340, 969, 1461, 1207, 762, 115, 1455, 1286, 856, 941, 328, 1085, 1361, 772, 687, 565, 515, 1490, 1411, 1055, 813, 1403, 606, 352, 291, 1474, 1489, 18, 343, 25, 1480, 399, 1311, 1504, 1272, 414, 660, 1431, 272, 1417, 1507, 1473, 1165, 344, 432, 1280, 358, 546, 243, 539, 988, 90, 531, 1357, 1467, 917, 104, 1068, 373, 983, 1169, 270, 691, 755, 1060, 1335, 878, 326, 1468, 1248, 101, 490, 1148, 278, 34, 588, 1040, 1174, 925, 1509, 403, 146, 527, 1136, 61, 263, 1235, 1486, 693, 767, 1510, 1354, 1020, 610, 1366, 1456, 1477, 411, 302, 659, 1459, 1360, 492, 1429, 366, 1032, 268, 898, 1215, 1312, 1099, 1121, 1428, 1373, 4, 1067, 1317, 29, 147, 895, 1375, 410, 859, 329, 1374, 1307, 1103, 1047, 1299, 1488, 416, 1419, 357, 629, 998, 1269, 94, 1242, 832, 397, 1157, 483, 1495, 1130, 638, 586, 303, 1338, 1010, 1475, 1296, 541, 1309, 81, 528, 786, 1420, 701, 353, 844, 1394, 648, 1503, 1380, 1087, 1231, 1399, 1151, 1131, 892, 900, 1350, 829, 1058, 42, 1092, 1476, 1500, 766, 888, 992, 417, 1313, 1346, 1039, 449, 122, 679, 360, 920, 440, 125, 805, 618, 870, 825, 235, 1277, 1225, 1290, 1446, 1401, 1511, 1200, 1155, 26, 867, 1266, 676, 92, 715, 1398, 1134, 1482, 1051, 798, 1426, 734, 1506, 17, 947, 1514, 1125, 212, 247, 800, 1481, 1293, 1056, 1501, 1143, 1512, 942, 1441, 1197, 1400, 1440, 893, 1109, 1364, 1437, 156, 228, 790, 1385, 716, 866, 336, 1323, 806, 443, 1491, 1232, 1057, 965, 1037, 577, 459, 1001, 184, 76, 761, 1107, 1520, 45, 1525, 1172, 1351, 1522, 778, 1519, 8, 1449, 1021, 719, 1465, 636, 456, 1045, 1496, 1024, 615, 821, 739, 547, 439, 1115, 1527, 1524, 1066, 764, 1295, 1259, 970, 557, 559, 1027, 1018, 645, 1533, 990, 802, 1078, 301, 1497, 855, 837, 1198, 161, 1161, 1209, 996, 646, 1324, 991, 1463, 1391, 1529, 1135, 1424, 740, 1408, 327, 1538, 780, 1472, 1539, 830, 1196, 1230, 556, 1416, 792, 857, 1193, 779, 1542, 735, 1541, 809, 421, 1397, 1544, 962, 1402, 674, 1548, 1528, 494, 924, 1554, 1515, 758, 333, 1556, 1549, 391, 1517, 118, 1508, 365, 1537, 1536, 1550, 1558, 1540, 136, 612, 488, 1422, 601, 1229, 1564, 1084, 1049, 350, 1518, 1471, 1567, 1563, 63, 1526, 1547, 1559, 1568, 853, 1572, 1505, 1562, 1546, 1478, 1578, 1566, 1579, 1570, 1531, 280, 1583, 1258, 799, 511, 1588, 550, 1573, 1575, 1586, 822, 1581, 760, 1318, 1594, 1597, 1592, 1580, 1483, 1530, 1355, 1605, 1532, 1603, 1598, 1604, 1602, 1577, 1593, 1595, 1610, 1599, 1612, 1601, 884, 1606, 978, 732, 810, 1571, 215, 1569, 868, 129, 1557, 1624, 1095, 598, 1625, 1181, 1555, 1630, 771, 473, 1647, 1635, 1623, 1611, 1613, 1626, 447, 1650, 1218, 1649, 819, 937, 989, 1614, 1640, 1584, 1648, 811, 1560, 1585, 1632, 1655, 1616, 1576, 1589, 1213, 1665, 1083, 1608, 1661, 1659, 1660, 1618, 1622, 1587, 1675, 1667, 1673, 1600, 1670, 1664, 651, 1671, 1679, 1634, 1590, 1662, 1672, 1688, 1565, 1638, 1689, 1629, 797, 1684, 1680, 143, 1221, 1621, 1668, 1683, 1561, 1692, 1543, 1695, 1596, 1644, 1607, 1666, 817, 1615, 1188, 1669, 1636, 1041, 1681, 1210, 1702, 1697, 1700, 1674, 1686, 1699, 1617, 1582, 1682, 1703, 1663, 1690, 1609, 1709, 1706, 1233, 1714, 1551, 1716, 1685, 1652, 1545, 1676, 1729, 543, 1727, 1637, 1696, 1687, 1705, 1711, 1730, 1731, 1724, 114, 1737, 1719, 1715, 1642, 460, 1704, 1656, 1738, 875, 1740, 1710, 1639, 1728, 1726, 611, 1717, 1732, 1713, 1677, 1762, 1756, 1720, 1759, 1751, 1742, 1764, 1763, 1773, 435, 1658, 1775, 1747, 1741, 1707, 1771, 1733, 1758, 1725, 589, 1722, 563, 1382, 1693, 1746, 1765, 1767, 1784, 1770, 1786, 285, 1761, 1782, 1788, 1752, 1744, 1708, 1793, 1792, 876, 1739, 1791, 1776, 1787, 843, 1790, 1783, 1777, 1678, 1774, 1795, 1657, 1789, 1753, 1766, 214, 1755, 650, 1749, 1769, 1721, 1781, 1802, 1803, 1805, 1796, 1117, 1365, 486, 1811, 1809, 1768, 1628, 1806, 1735, 1812, 1801, 1816, 1743, 1799, 1825, 1820, 1778, 1804, 1772, 1808, 1824, 142, 1810, 1829, 1826, 1815, 1833, 1834, 1798, 1837, 1831, 1807, 1819, 1830, 1748, 1847, 1813, 1839, 1852, 1841, 1832, 938, 1750, 1854, 845, 1859, 1821, 1838, 1698, 1858, 1853, 1818, 1860, 1857, 1862, 1828, 1850, 1835, 1694, 1785, 1845, 1823, 1864, 1866, 1840, 1574, 1836, 1867, 1861, 1872, 1843, 1633, 1875, 1873, 462, 1877, 1884, 1865, 1863, 1886, 1888, 1870, 1878, 1701, 1848, 1880, 1887, 1827, 1897, 1116, 1885, 1846, 1902, 1891, 1883, 1900, 1822, 1910, 1911, 1871, 1914, 1908, 1173, 1913, 1909, 1918, 1912, 1876, 1916, 1922, 1927, 1928, 1924, 1925, 1931, 1881, 1937, 1932, 1936, 1736, 1934, 1921, 1915, 1907, 1941, 1943, 1920, 1940, 1938, 1930, 1944, 1935, 1896, 1939, 1855, 1285, 1951, 1948, 1957, 1950, 1949, 1958, 1933, 1874, 773, 1964, 1905, 1942, 1946, 1965, 1955, 1970, 1800, 1967, 1977, 1961, 865, 1466, 1929, 1926, 1982, 1534, 1919, 1899, 1893, 1779, 1966, 1985, 1960, 1989, 1991, 1999, 1996, 1959, 1978, 1997, 2002, 2001, 1994, 2003, 1986, 1983, 2000, 2004, 1990, 2007, 1956, 1995, 2015, 2014, 2012, 2005, 1945, 1780, 2011, 2021, 1984, 2019, 1947, 1998, 2024, 2016, 2023, 2008, 2025, 2010, 2017, 2013, 1552, 2018, 2028, 1904, 1968, 2026, 2030, 1952, 1794, 2032, 2031, 1962, 2027, 1869, 1993, 1971, 2006, 2036, 2022, 2044, 2049, 1976, 2046, 2052, 2040, 2043, 2048, 2047, 1988, 1892, 1745, 1972, 1754, 418, 2009, 2029, 2059, 2051, 2033, 2058, 1691, 2039, 2061, 65, 2070, 2068, 2072, 2060, 2057, 1954, 2064, 2077, 2073, 2053, 2050, 2034, 2041, 1851, 2082, 2085, 2075, 2078, 2083, 2042, 2086, 2079, 2089, 1856, 2095, 2037, 2090, 2087, 2080, 2081, 2101, 2100, 2094, 310, 2097, 1980, 2054, 1180, 1969, 685, 2055, 2099, 927, 2092, 2108, 2105, 2056, 2111, 1124, 2103, 2114, 2107, 2084, 2066, 2093, 2110, 2038, 2122, 2127, 2117, 2119, 2063, 2071, 2123, 2126, 2129, 2062, 2069, 2141, 2131, 1975, 2137, 2134, 2125, 2143, 2138, 2133, 2148, 2139, 2135, 2149, 1760, 2067]
unique_charter_type = [1, 0, 2]
unique_country_name = ['Greece', 'France', 'Croatia', 'Italy', 'Norway', 'Seychelles', 'Spain', 'Thailand', 'Guadeloupe', 'Martinique', 'Turkey', 'New Caledonia', 'United States', 'Saint Lucia', 'Puerto Rico', 'French Polynesia', 'Malta', 'Malaysia', 'Cuba', 'Netherlands', 'Morocco', 'Dominican Republic', 'British Virgin Islands', 'Belize', 'Australia', 'Saint Martin', 'Madagascar', 'The Bahamas', 'Argentina', 'Panama', 'Belgium', 'Cape Verde', 'Portugal', 'Antigua and Barbuda', 'Montenegro', 'Brazil', 'Saint Vincent and the Grenadines', 'Grenada', 'Sweden', 'Mexico', 'Denmark', 'Venezuela', 'Philippines', 'Germany', 'Slovenia', 'Maldives', 'Singapore', 'Tunisia', 'Mauritius', 'United Kingdom', 'Indonesia', 'Senegal', 'Fiji', 'Estonia', 'Finland', 'Ireland', 'Canada', 'Sri Lanka', 'Lithuania', 'Egypt', 'United Arab Emirates', 'Ecuador', 'Myanmar', 'Bermuda', 'Colombia', 'India', 'Poland', 'China', 'Vietnam', 'Japan', 'Greenland', 'Iceland', 'Palau', 'Romania', 'Anguilla', 'Mayotte', 'Tanzania', 'Mozambique', 'Oman', 'Tonga', 'Albania', 'Chile', 'Cyprus', 'Dominica', 'Barbados', 'Zambia', 'Hungary', 'Netherlands Antilles', 'Antarctica']
unique_destination_flexible = [0, 1]
unique_flexible_date = [3, 0, 7, 1]
unique_request_date_day = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
unique_month_request = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
unique_day_time_request = ['morning', 'afternoon', 'evening', 'night']
unique_days_before_departure = [178, 190, 211, 162, 127, 197, 57, 155, 64, 176, 183, 85, 22, 92, 30, 8, 189, 106, 141, 177, 246, 170, 128, 43, 18, 330, 111, 63, 196, 182, 17, 175, 119, 191, 89, 174, 97, 161, 200, 84, 210, 112, 105, 140, 34, 58, 35, 147, 294, 88, 188, 133, 154, 231, 168, 198, 238, 74, 16, 195, 146, 62, 144, 15, 104, 202, 139, 118, 181, 160, 55, 167, 184, 54, 151, 37, 1, 125, 36, 0, 192, 96, 153, 193, 166, 187, 129, 222, 149, 180, 138, 236, 173, 87, 152, 169, 82, 103, 186, 369, 108, 60, 109, 145, 201, 194, 40, 131, 350, 159, 179, 228, 81, 10, 242, 158, 99, 114, 66, 120, 4, 172, 116, 150, 53, 130, 235, 6, 67, 102, 100, 59, 157, 199, 24, 52, 115, 206, 321, 122, 80, 185, 171, 164, 79, 255, 290, 143, 98, 165, 136, 163, 101, 95, 135, 65, 208, 86, 212, 226, 110, 72, 317, 9, 93, 134, 77, 360, 218, 50, 71, 148, 83, 137, 224, 91, 286, 90, 126, 132, 329, 343, 28, 94, 69, 223, 313, 229, 5, 124, 11, 156, 75, 117, 311, 51, 41, 123, 113, 207, 220, 367, 33, 205, 3, 68, 78, 312, 142, 219, 389, 107, 49, 204, 31, 29, 76, 42, 27, 483, 209, 216, 12, 227, 258, 213, 19, 61, 26, 453, 278, 45, 221, 73, 39, 244, 326, 44, 25, 70, 48, 234, 121, 260, 225, 217, 300, 309, 274, 315, 47, 265, 256, 585, 13, 269, 297, 324, 233, 254, 469, 32, 230, 20, 56, 600, 257, 263, 418, 307, 38, 46, 2, 295, 203, 342, 306, 375, 547, 515, 23, 21, 520, 14, 327, 241, 293, 435, 394, 279, 250, 522, 308, 239, 277, 7, 474, 413, 272, 494, 411, 264, 296, 259, 395, 404, 276, 325, 385, 280, 640, 486, 334, 337, 442, 232, 386, 245, 359, 412, 240, 305, 451, 248, 289, 316, 421, 266, 267, 407, 339, 281, 495, 383, 271, 377, 445, 388, 249, 338, 561, 498, 553, 651, 461, 291, 452, 214, 319, 391, 410, 320, 270, 333, 524, 318, 450, 402, 584, 406, 237, 409, 268, 348, 215, 419, 354, 380, 408, 416, 397, 401, 392, 568, 355, 376, 487, 357, 364, 427, 253, 384, 349, 362, 340, 347, 374, 365, 252, 439, 399, 285, 396, 292, 446, 361, 363, 465, 283, 373, 247, 282, 351, 379, 432, 403, 443, 261, 322, 287, 398, 425, 314, 481, 423, 328, 430, 284, 262, 366, 344, 378, 371, 341, 724, 444, 332, 331, 353, 310, 298, 323, 414, 356, 405, 299, 346, 275, 426, 460, 381, 422, 303, 393, 288, 336, 304, 358, 335, 475, 370, 273, 466, 345, 368, 352, 302, 372, 301, 457, 251, 506, 615, 489, 243, 467, 668, 436, 459, 437, 537, 589, 657, 649, 470, 635, 541, 557, 645, 516, 500, 562, 503, 582, 599, 488, 480, 482, 523, 613, 478, 382, 472, 511, 499, 550, 485, 492, 455, 479, 508, 438, 504, 501, 521, 417, 424, 464, -5, 471, 433, 490, 476, 458, 512, 441, 513, 390, 468, 429, 420, 545, 387, 431, 434, 428, 400, 502, 456, 415, 718, 510, 583, 669, 641, 650, 449, 618, 629, 688, 580, 573, 527, 558, 642, 534, 608, 619, 544, 624, 509, 710, 556, 539, 548, 567, 526, 555, 529, 528, 549, 493, 706, 454, 462, 631, 514, 551, 530, 610, 440, 484, 496, 664, 491, 448, 447, 726, 542, 684, 676, 675, 690, 652, 672, 656, 667, 592, 663, 607, 587, 525, 605, 563, 602, 554, 579, 564, 543, 593, 565, 497, 540, 566, 477, 518, 473, 535, 519, 560, 517, 725, 612, 532, 536, 717, 531, 714, 727, 653, 720, 628, 662, -17756, 637, 719, 708, 655, -17790, -17791, 623, 636, 627, 666, 712, 559, 507, 614, 606, 670, 552, 702, 463, 646, 609, 654, 604, 648, 578, 581, 576, 577, 569, 538, 586, 597, 601, 723, 505, 533, 546, 575, -17916, 590, 634, 572, 705, 686, 678, 685, 673, 633, 588, 665, 638, 643, 681, 617, 598, 611, 674, 687, 571, 625, 616, 591, 626, 679, 700, -18451, 630, 721, 722, 639, 694, 603, 693, 570, 574, 715, -18812, 701, -18836, 691, 697, 661, 621, 677, 594, 622, -19087, 695, -19183]
unique_in_europe = [1, 0]
unique_num_passengers = [7, 8, 4, 6, 2, 3, 5, 1, 9, 10, 12, 13, 19, 11, 14, 21, 18, 15, 16, 23, 17, 20, 26, 25, 31, 27, 22, 42, 34, 28, 24, 33, 35, 41, 0, 30, 29, 37, 38, 36, 39, 40, 32]
unique_kid_on_board = [1, 0]
unique_duration = [5, 7, 14, 6, 2, 1, 10, 12, 8, 0, 3, 11, 13, 9, 21, 4, 15, 18, 28, 17, 19, 22, 16, 20, 26, 25, 23, 24, 27]
unique_civility = ['Ms', 'Mr']
unique_country_name_us = ['Spain', 'Germany', 'United Kingdom', 'Italy', 'France', 'Sweden', 'Belgium', 'Austria', 'Brazil', 'Switzerland', 'Australia', 'Russia', 'Canada', 'Bulgaria', 'Uruguay', 'Montenegro', 'Colombia', 'United States', 'Norway', 'Poland', 'Martinique', 'Finland', 'Argentina', 'Netherlands', 'Singapore', 'French Polynesia', 'Iceland', 'Portugal', 'New Caledonia', 'Mayotte', 'South Africa', 'Romania', 'Morocco', 'Turkey', 'Denmark', 'Chile', 'New Zealand', 'Dominican Republic', 'Armenia', 'Slovakia', 'Qatar', 'Ireland', 'Guadeloupe', 'Croatia', 'Greece', 'Israel', 'Mexico', 'Serbia', 'Hong Kong', 'India', 'Luxembourg ', 'Cyprus', 'Peru', 'Venezuela', 'Former Yugoslav Republic of Macedonia', 'Lithuania', "C�te d'Ivoire", 'Ukraine', 'Albania', 'Slovenia', 'Puerto Rico', 'Jordan', 'Czech Republic', 'R�union', 'United Arab Emirates', 'Thailand', 'French Guiana', 'Monaco', 'Gabon', 'Malaysia', 'San Marino', 'Philippines', 'Hungary', 'Saint Martin', 'Latvia', 'Egypt', 'Panama', 'Kenya', 'Tunisia', 'Lebanon', 'Ecuador', 'Moldova', 'Estonia', 'Kuwait', 'China', 'Bosnia and Herzegovina', 'South Korea', 'Guatemala', 'Japan', 'Indonesia', 'Costa Rica', 'Saudi Arabia', 'Oman', 'Georgia', 'Malta', 'Pakistan', 'Bahrain', 'Gibraltar', 'The Bahamas', 'Bolivia', 'Kazakhstan', 'Madagascar', 'Seychelles', 'Burundi', 'Belarus', 'Andorra', 'Azerbaijan', 'Ghana', 'Cape Verde', 'Mauritania', 'US Virgin Islands', 'Nigeria', 'Turkmenistan', 'Papua New Guinea', 'Taiwan', 'Iran', 'Paraguay', 'Algeria', 'Senegal', 'Laos', 'El Salvador', 'Mauritius', 'Macau', 'Myanmar', 'Haiti', 'S?o Tom� and Pr�ncipe', 'Cayman Islands', 'Faeroe Islands', 'Tanzania', 'Swaziland', 'Benin', 'Sri Lanka', 'Saint Kitts and Nevis', 'Barbados', 'Saint Vincent and the Grenadines', 'Zambia', 'Vanuatu', 'Democratic Republic of the Congo', 'Liechtenstein', 'Trinidad and Tobago', 'Congo', 'Guam', 'Saint Pierre and Miquelon', 'Antigua and Barbuda', 'Saint Lucia', 'Belize', 'Ethiopia', 'Nepal', 'Uzbekistan', 'Niue', 'Uganda', 'Cameroon', 'Bermuda', 'Zimbabwe', 'Dominica', 'United States Minor Outlying Islands', 'Brunei', 'Honduras', 'Cook Islands', 'Cuba', 'Christmas Island', 'Vietnam', 'British Virgin Islands', 'Micronesia', 'Netherlands Antilles', 'Jamaica', 'Aruba', 'Mongolia', 'Afghanistan', 'Maldives', 'Tuvalu', 'Namibia', 'Botswana', 'Malawi', 'Mozambique', 'Syria', 'Antarctica', 'Mali', 'Sierra Leone', 'Angola', 'Bangladesh', 'Iraq', 'Anguilla', 'Grenada', 'Montserrat', 'Eritrea', 'Northern Marianas', 'Kyrgyzstan', 'Yemen', 'Central African Republic', 'Solomon Islands', 'Greenland', 'Rwanda', 'The Gambia', 'South Georgia and the South Sandwich Islands', 'Cambodia', 'Tajikistan', 'Somalia', 'Sudan', 'Fiji']
unique_is_mac = [1, 0]


# Set the URL for your images
image_url = 'https://www.leadingresults.com/hs-fs/hubfs/Blog_Images/Ramblings/choose%20the%20right%20customer.jpg?width=788&name=choose%20the%20right%20customer.jpg'
image_url_side = 'https://www.leadingresults.com/hs-fs/hubfs/Blog_Images/Ramblings/choose%20the%20right%20customer.jpg?width=788&name=choose%20the%20right%20customer.jpg'

#Colomns 
col1, col2, col3 = st.columns(3)
col1.metric("Best performing model", "RANDOM FOREST")
col2.metric("Final dataset", "164 893 rows")
col3.metric("Number of features", "17")

# Add the image to the center part of app
#st.image(image_url, width=500)

st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>What is the probability of booking?</h1>", unsafe_allow_html=True)

# Add the image to the side part of app
st.sidebar.image(image_url_side, width=300)

st.sidebar.header("Create a fictional client")


# Define function to preprocess data
def preprocess_data(input_data):
    # Preprocess data as needed, return features as array
    # This is just an example; you would replace this with your own preprocessing function
    num_passengers = input_data['num_passengers']
    country_name = input_data['country_name']
    civility = input_data['civility']
    day_time_request = input_data['day_time_request']

    features = np.array([num_passengers, country_name, civility, day_time_request]).reshape(1, -1)
    return features

# Define function to get model predictions
def get_predictions(features):    #API
    # Use your trained linear regression model to get predictions for given input features
    # This is just an example; you would replace this with your own prediction function
    
    try:
        model = LinearRegression()
        model.fit(X_train, y_train)
        prediction = model.predict(features)
    except:
        prediction = 0.85
        
    return prediction

# Define form fields
input_fields = {
    #Profile of client
    'is_new_user'  : st.sidebar.radio("Is it a new user?", unique_is_new_user),
    'country_name_us': st.sidebar.selectbox('Country of client', unique_country_name_us),
    'civility': st.sidebar.radio('Sex', unique_civility),
    'is_mac': st.sidebar.radio('Mac user?', unique_is_mac),

    #Info about trip
    'num_passengers': st.sidebar.slider('Number of passengers', 0, 2, max(unique_num_passengers)),
    'kid_on_board': st.sidebar.radio('Are there kids?', unique_kid_on_board),
    'in_europe'  : st.sidebar.radio("Travel in Europe?:", unique_in_europe),
    'duration': st.sidebar.slider('Duration of trip', 0, 2, max(unique_duration)),
    'destination_flexible'  : st.sidebar.radio("Is the trip flexible?:", unique_destination_flexible),
    'country_name'  : st.sidebar.selectbox("Destination of trip?", unique_country_name),
    'flexible_date'  : st.sidebar.selectbox("Are dates flexible?", unique_flexible_date),

    #Info about rental
    'id_charter_company': st.sidebar.selectbox('Renter of the boat', unique_id_charter_company),
    'charter_type': st.sidebar.radio('Type of rental', unique_charter_type),
    
    #Info about request
    'request_date_day': st.sidebar.selectbox('Day of week of the request', unique_request_date_day),
    'month_request': st.sidebar.selectbox('Month of the request', unique_month_request),
    'day_time_request': st.sidebar.selectbox('Period of day of the request', unique_day_time_request),
    'days_before_departure': st.sidebar.slider('Days before departure', 0, 2, max(unique_days_before_departure))

}

# Create form and submit button
form = st.form(key='my_form')
with form:
    submit_button = st.form_submit_button(label='Submit')

# When form is submitted, preprocess input data and get model predictions
if submit_button:   #request.get
    input_data = pd.Series(input_fields)
    features = preprocess_data(input_data)
    prediction = get_predictions(features)

    # Display prediction in fancy way using Plotly
    fig = px.pie(values=[prediction, 1-prediction], names=['Probability of Booking', 'Probability of Not Booking'])
    st.plotly_chart(fig)
    
# Instrukcja warunkowa if-elif-else
#if submit_button and prediction > 0.70:
#    st.success('It is very likely that this is a valuable customer! Contact him in priority!')
#elif prediction < 0.70 and prediction > 0.50:
#    st.warning('This is a semi success')
#else:
#    st.error('Maybe better to focus on other clients firstly!')
