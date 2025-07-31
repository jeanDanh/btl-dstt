import sys 
sys.path.append("./backend/")
from DataManager import DataManager

def main():
	data_mag = DataManager()

	# nhom A
	data_mag.addPurchaseData( 'C000', 'P000', 2 )
	data_mag.addPurchaseData( 'C001', 'P000', 1 )
	data_mag.addPurchaseData( 'C004', 'P000', 2 )
	data_mag.addPurchaseData( 'C008', 'P000', 2 )
	data_mag.addPurchaseData( 'C009', 'P000', 3 )

	data_mag.addPurchaseData( 'C001', 'P001', 4 )
	data_mag.addPurchaseData( 'C004', 'P001', 3 )
	data_mag.addPurchaseData( 'C008', 'P001', 3 )

	data_mag.addPurchaseData( 'C000', 'P002', 2 )
	data_mag.addPurchaseData( 'C001', 'P002', 1 )
	data_mag.addPurchaseData( 'C004', 'P002', 2 )
	data_mag.addPurchaseData( 'C005', 'P002', 1 )
	data_mag.addPurchaseData( 'C008', 'P002', 3 )
	data_mag.addPurchaseData( 'C009', 'P002', 1 )

	data_mag.addPurchaseData( 'C000', 'P003', 3 )
	data_mag.addPurchaseData( 'C005', 'P003', 4 )
	data_mag.addPurchaseData( 'C008', 'P003', 3 )

	data_mag.addPurchaseData( 'C008', 'P004', 4 )
	data_mag.addPurchaseData( 'C009', 'P004', 6 )

	data_mag.addPurchaseData( 'C009', 'P005', 5 )
	data_mag.addPurchaseData( 'C000', 'P005', 5 )

	data_mag.addPurchaseData( 'C000', 'P006', 4 )
	data_mag.addPurchaseData( 'C001', 'P006', 3 )
	data_mag.addPurchaseData( 'C004', 'P006', 1 )
	data_mag.addPurchaseData( 'C009', 'P006', 2 )

	data_mag.addPurchaseData( 'C001', 'P007', 4 )
	data_mag.addPurchaseData( 'C004', 'P007', 6 )

	data_mag.addPurchaseData( 'C000', 'P008', 1 )
	data_mag.addPurchaseData( 'C001', 'P008', 2 )
	data_mag.addPurchaseData( 'C004', 'P008', 3 )
	data_mag.addPurchaseData( 'C005', 'P008', 2 )
	data_mag.addPurchaseData( 'C009', 'P008', 2 )

	data_mag.addPurchaseData( 'C005', 'P009', 5 )
	data_mag.addPurchaseData( 'C008', 'P009', 5 )

	data_mag.addPurchaseData( 'C008', 'P010', 9 )

	data_mag.addPurchaseData( 'C009', 'P011', 3 )
	data_mag.addPurchaseData( 'C000', 'P011', 7 )

	data_mag.addPurchaseData( 'C000', 'P093', 1 )
	data_mag.addPurchaseData( 'C001', 'P093', 2 )
	data_mag.addPurchaseData( 'C004', 'P093', 1 )
	data_mag.addPurchaseData( 'C005', 'P093', 2 )
	data_mag.addPurchaseData( 'C008', 'P093', 3 )
	data_mag.addPurchaseData( 'C009', 'P093', 1 )

	data_mag.addPurchaseData( 'C001', 'P094', 1 )
	data_mag.addPurchaseData( 'C004', 'P094', 3 )
	data_mag.addPurchaseData( 'C005', 'P094', 3 )
	data_mag.addPurchaseData( 'C009', 'P094', 3 )

	data_mag.addPurchaseData( 'C000', 'P095', 1 )
	data_mag.addPurchaseData( 'C001', 'P095', 3 )
	data_mag.addPurchaseData( 'C004', 'P095', 2 )
	data_mag.addPurchaseData( 'C005', 'P095', 1 )
	data_mag.addPurchaseData( 'C009', 'P095', 3 )

	data_mag.addPurchaseData( 'C001', 'P096', 3 )
	data_mag.addPurchaseData( 'C005', 'P096', 4 )
	data_mag.addPurchaseData( 'C008', 'P096', 3 )

	data_mag.addPurchaseData( 'C008', 'P097', 5 )
	data_mag.addPurchaseData( 'C009', 'P097', 4 )
	
	data_mag.addPurchaseData( 'C000', 'P098', 3 )
	data_mag.addPurchaseData( 'C001', 'P098', 2 )
	data_mag.addPurchaseData( 'C005', 'P098', 3 )
	data_mag.addPurchaseData( 'C009', 'P098', 2 )


	# nhom B
	data_mag.addPurchaseData( 'C006', 'P052', 2 )
	data_mag.addPurchaseData( 'C007', 'P052', 2 )
	data_mag.addPurchaseData( 'C011', 'P052', 1 )
	data_mag.addPurchaseData( 'C010', 'P052', 1 )
	data_mag.addPurchaseData( 'C017', 'P052', 3 )
	data_mag.addPurchaseData( 'C018', 'P052', 1 )

	data_mag.addPurchaseData( 'C010', 'P053', 4 )
	data_mag.addPurchaseData( 'C017', 'P053', 2 )
	data_mag.addPurchaseData( 'C018', 'P053', 4 )

	data_mag.addPurchaseData( 'C006', 'P054', 1 )
	data_mag.addPurchaseData( 'C007', 'P054', 3 )
	data_mag.addPurchaseData( 'C011', 'P054', 4 )
	data_mag.addPurchaseData( 'C017', 'P054', 2 )

	data_mag.addPurchaseData( 'C006', 'P055', 6 )
	data_mag.addPurchaseData( 'C010', 'P055', 4 )

	data_mag.addPurchaseData( 'C006', 'P056', 2 )
	data_mag.addPurchaseData( 'C007', 'P056', 3 )
	data_mag.addPurchaseData( 'C010', 'P056', 2 )
	data_mag.addPurchaseData( 'C011', 'P056', 2 )
	data_mag.addPurchaseData( 'C018', 'P056', 1 )

	data_mag.addPurchaseData( 'C011', 'P057', 5 )
	data_mag.addPurchaseData( 'C017', 'P057', 5 )

	data_mag.addPurchaseData( 'C007', 'P058', 2 )
	data_mag.addPurchaseData( 'C011', 'P058', 3 )
	data_mag.addPurchaseData( 'C010', 'P058', 5 )

	data_mag.addPurchaseData( 'C006', 'P059', 4 )
	data_mag.addPurchaseData( 'C007', 'P059', 6 )

	data_mag.addPurchaseData( 'C010', 'P060', 2 )
	data_mag.addPurchaseData( 'C017', 'P060', 3 )
	data_mag.addPurchaseData( 'C018', 'P060', 5 )

	data_mag.addPurchaseData( 'C006', 'P061', 6 )
	data_mag.addPurchaseData( 'C011', 'P061', 1 )
	data_mag.addPurchaseData( 'C010', 'P061', 3 )

	data_mag.addPurchaseData( 'C006', 'P062', 2 )
	data_mag.addPurchaseData( 'C007', 'P062', 4 )
	data_mag.addPurchaseData( 'C010', 'P062', 3 )
	data_mag.addPurchaseData( 'C011', 'P062', 1 )

	data_mag.addPurchaseData( 'C007', 'P063', 3 )
	data_mag.addPurchaseData( 'C011', 'P063', 3 )
	data_mag.addPurchaseData( 'C017', 'P063', 4 )

	data_mag.addPurchaseData( 'C006', 'P064', 1 )
	data_mag.addPurchaseData( 'C010', 'P064', 4 )
	data_mag.addPurchaseData( 'C011', 'P064', 4 )
	data_mag.addPurchaseData( 'C018', 'P064', 1 )

	data_mag.addPurchaseData( 'C007', 'P065', 2 )
	data_mag.addPurchaseData( 'C010', 'P065', 1 )
	data_mag.addPurchaseData( 'C011', 'P065', 3 )
	data_mag.addPurchaseData( 'C017', 'P065', 2 )
	data_mag.addPurchaseData( 'C018', 'P065', 2 )

	data_mag.addPurchaseData( 'C010', 'P066', 5 )
	data_mag.addPurchaseData( 'C018', 'P066', 5 )

	data_mag.addPurchaseData( 'C006', 'P067', 1 )
	data_mag.addPurchaseData( 'C007', 'P067', 3 )
	data_mag.addPurchaseData( 'C010', 'P067', 2 )
	data_mag.addPurchaseData( 'C018', 'P067', 4 )

	data_mag.addPurchaseData( 'C011', 'P068', 6 )
	data_mag.addPurchaseData( 'C010', 'P068', 4 )

	data_mag.addPurchaseData( 'C006', 'P069', 3 )
	data_mag.addPurchaseData( 'C007', 'P069', 5 )
	data_mag.addPurchaseData( 'C011', 'P069', 2 )

	data_mag.addPurchaseData( 'C010', 'P070', 5 )
	data_mag.addPurchaseData( 'C017', 'P070', 5 )

	data_mag.addPurchaseData( 'C006', 'P071', 3 )
	data_mag.addPurchaseData( 'C007', 'P071', 2 )
	data_mag.addPurchaseData( 'C011', 'P071', 4 )
	data_mag.addPurchaseData( 'C018', 'P071', 1 )

	data_mag.addPurchaseData( 'C006', 'P072', 2 )
	data_mag.addPurchaseData( 'C007', 'P072', 2 )
	data_mag.addPurchaseData( 'C010', 'P072', 1 )
	data_mag.addPurchaseData( 'C011', 'P072', 3 )
	data_mag.addPurchaseData( 'C017', 'P072', 2 )


	# nhom C
	data_mag.addPurchaseData( 'C002', 'P025', 2 )
	data_mag.addPurchaseData( 'C003', 'P025', 1 )
	data_mag.addPurchaseData( 'C012', 'P025', 3 )
	data_mag.addPurchaseData( 'C014', 'P025', 1 )
	data_mag.addPurchaseData( 'C015', 'P025', 2 )
	data_mag.addPurchaseData( 'C019', 'P025', 1 )
	
	data_mag.addPurchaseData( 'C003', 'P026', 3 )
	data_mag.addPurchaseData( 'C013', 'P026', 2 )
	data_mag.addPurchaseData( 'C015', 'P026', 2 )
	data_mag.addPurchaseData( 'C016', 'P026', 3 )

	data_mag.addPurchaseData( 'C002', 'P027', 4 )
	data_mag.addPurchaseData( 'C014', 'P027', 3 )
	data_mag.addPurchaseData( 'C016', 'P027', 2 )
	data_mag.addPurchaseData( 'C019', 'P027', 1 )

	data_mag.addPurchaseData( 'C003', 'P028', 4 )
	data_mag.addPurchaseData( 'C015', 'P028', 1 )
	data_mag.addPurchaseData( 'C012', 'P028', 3 )
	data_mag.addPurchaseData( 'C019', 'P028', 2 )

	data_mag.addPurchaseData( 'C003', 'P029', 1 )
	data_mag.addPurchaseData( 'C013', 'P029', 3 )
	data_mag.addPurchaseData( 'C014', 'P029', 5 )
	data_mag.addPurchaseData( 'C019', 'P029', 1 )

	data_mag.addPurchaseData( 'C002', 'P030', 1 )
	data_mag.addPurchaseData( 'C012', 'P030', 4 )
	data_mag.addPurchaseData( 'C013', 'P030', 2 )
	data_mag.addPurchaseData( 'C015', 'P030', 3 )
	data_mag.addPurchaseData( 'C016', 'P030', 1 )

	data_mag.addPurchaseData( 'C019', 'P031', 2 )
	data_mag.addPurchaseData( 'C015', 'P031', 5 )
	data_mag.addPurchaseData( 'C003', 'P031', 3 )

	data_mag.addPurchaseData( 'C012', 'P032', 1 )
	data_mag.addPurchaseData( 'C014', 'P032', 5 )
	data_mag.addPurchaseData( 'C013', 'P032', 3 )
	data_mag.addPurchaseData( 'C002', 'P032', 1 )

	data_mag.addPurchaseData( 'C016', 'P033', 3 )
	data_mag.addPurchaseData( 'C012', 'P033', 4 )
	data_mag.addPurchaseData( 'C015', 'P033', 3 )

	data_mag.addPurchaseData( 'C003', 'P034', 1 )
	data_mag.addPurchaseData( 'C013', 'P034', 2 )
	data_mag.addPurchaseData( 'C014', 'P034', 1 )
	data_mag.addPurchaseData( 'C016', 'P034', 3 )
	data_mag.addPurchaseData( 'C019', 'P034', 3 )

	data_mag.addPurchaseData( 'C002', 'P035', 1 )
	data_mag.addPurchaseData( 'C003', 'P035', 2 )
	data_mag.addPurchaseData( 'C013', 'P035', 3 )
	data_mag.addPurchaseData( 'C014', 'P035', 1 )
	data_mag.addPurchaseData( 'C016', 'P035', 3 )

	data_mag.addPurchaseData( 'C002', 'P036', 1 )
	data_mag.addPurchaseData( 'C012', 'P036', 2 )
	data_mag.addPurchaseData( 'C013', 'P036', 1 )
	data_mag.addPurchaseData( 'C014', 'P036', 2 )
	data_mag.addPurchaseData( 'C015', 'P036', 1 )
	data_mag.addPurchaseData( 'C019', 'P036', 3 )

	data_mag.addPurchaseData( 'C012', 'P037', 2 )
	data_mag.addPurchaseData( 'C013', 'P037', 3 )
	data_mag.addPurchaseData( 'C014', 'P037', 2 )
	data_mag.addPurchaseData( 'C019', 'P037', 2 )

	data_mag.addPurchaseData( 'C003', 'P038', 1 )
	data_mag.addPurchaseData( 'C012', 'P038', 2 )
	data_mag.addPurchaseData( 'C013', 'P038', 2 )
	data_mag.addPurchaseData( 'C014', 'P038', 2 )
	data_mag.addPurchaseData( 'C015', 'P038', 1 )
	data_mag.addPurchaseData( 'C016', 'P038', 2 )

	data_mag.addPurchaseData( 'C002', 'P039', 3 )
	data_mag.addPurchaseData( 'C016', 'P039', 3 )
	data_mag.addPurchaseData( 'C019', 'P039', 4 )

	data_mag.addPurchaseData( 'C012', 'P040', 3 )
	data_mag.addPurchaseData( 'C013', 'P040', 2 )
	data_mag.addPurchaseData( 'C014', 'P040', 3 )
	data_mag.addPurchaseData( 'C015', 'P040', 2 )

	data_mag.addPurchaseData( 'C003', 'P041', 3 )
	data_mag.addPurchaseData( 'C013', 'P041', 3 )
	data_mag.addPurchaseData( 'C019', 'P041', 4 )

	data_mag.addPurchaseData( 'C002', 'P042', 2 )
	data_mag.addPurchaseData( 'C013', 'P042', 2 )
	data_mag.addPurchaseData( 'C015', 'P042', 2 )
	data_mag.addPurchaseData( 'C016', 'P042', 2 )
	data_mag.addPurchaseData( 'C019', 'P042', 2 )

	data_mag.addPurchaseData( 'C003', 'P043', 2 )
	data_mag.addPurchaseData( 'C013', 'P043', 3 )
	data_mag.addPurchaseData( 'C014', 'P043', 2 )
	data_mag.addPurchaseData( 'C016', 'P043', 3 )

	data_mag.addPurchaseData( 'C012', 'P044', 2 )
	data_mag.addPurchaseData( 'C014', 'P044', 3 )
	data_mag.addPurchaseData( 'C015', 'P044', 3 )
	data_mag.addPurchaseData( 'C019', 'P044', 2 )

	data_mag.addPurchaseData( 'C002', 'P045', 3 )
	data_mag.addPurchaseData( 'C003', 'P045', 2 )
	data_mag.addPurchaseData( 'C014', 'P045', 2 )
	data_mag.addPurchaseData( 'C016', 'P045', 3 )

	data_mag.addPurchaseData( 'C012', 'P046', 3 )
	data_mag.addPurchaseData( 'C013', 'P046', 3 )
	data_mag.addPurchaseData( 'C014', 'P046', 2 )
	data_mag.addPurchaseData( 'C019', 'P046', 2 )

	data_mag.addPurchaseData( 'C002', 'P047', 2 )
	data_mag.addPurchaseData( 'C014', 'P047', 2 )
	data_mag.addPurchaseData( 'C015', 'P047', 2 )
	data_mag.addPurchaseData( 'C016', 'P047', 2 )
	data_mag.addPurchaseData( 'C019', 'P047', 2 )

	data_mag.addPurchaseData( 'C003', 'P048', 3 )
	data_mag.addPurchaseData( 'C012', 'P048', 3 )
	data_mag.addPurchaseData( 'C014', 'P048', 4 )

	data_mag.addPurchaseData( 'C002', 'P049', 2 )
	data_mag.addPurchaseData( 'C013', 'P049', 3 )
	data_mag.addPurchaseData( 'C015', 'P049', 3 )
	data_mag.addPurchaseData( 'C019', 'P049', 2 )

	data_mag.addPurchaseData( 'C012', 'P050', 3 )
	data_mag.addPurchaseData( 'C015', 'P050', 4 )
	data_mag.addPurchaseData( 'C016', 'P050', 3 )

	data_mag.addPurchaseData( 'C003', 'P051', 2 )
	data_mag.addPurchaseData( 'C014', 'P051', 1 )
	data_mag.addPurchaseData( 'C015', 'P051', 2 )
	data_mag.addPurchaseData( 'C016', 'P051', 2 )
	data_mag.addPurchaseData( 'C019', 'P051', 3 )

	data_mag.addPurchaseData( 'C002', 'P073', 3 )
	data_mag.addPurchaseData( 'C012', 'P073', 2 )
	data_mag.addPurchaseData( 'C013', 'P073', 3 )
	data_mag.addPurchaseData( 'C014', 'P073', 2 )

	data_mag.addPurchaseData( 'C002', 'P074', 2 )
	data_mag.addPurchaseData( 'C003', 'P074', 3 )
	data_mag.addPurchaseData( 'C012', 'P074', 2 )
	data_mag.addPurchaseData( 'C016', 'P074', 3 )

	data_mag.addPurchaseData( 'C002', 'P075', 3 )
	data_mag.addPurchaseData( 'C003', 'P075', 2 )
	data_mag.addPurchaseData( 'C012', 'P075', 2 )
	data_mag.addPurchaseData( 'C019', 'P075', 3 )

	data_mag.addPurchaseData( 'C013', 'P076', 4 )
	data_mag.addPurchaseData( 'C015', 'P076', 4 )
	data_mag.addPurchaseData( 'C016', 'P076', 2 )

	data_mag.addPurchaseData( 'C002', 'P077', 2 )
	data_mag.addPurchaseData( 'C003', 'P077', 3 )
	data_mag.addPurchaseData( 'C014', 'P077', 2 )
	data_mag.addPurchaseData( 'C019', 'P077', 3 )

	data_mag.addPurchaseData( 'C012', 'P078', 1 )
	data_mag.addPurchaseData( 'C013', 'P078', 3 )
	data_mag.addPurchaseData( 'C015', 'P078', 4 )
	data_mag.addPurchaseData( 'C016', 'P078', 2 )

	data_mag.addPurchaseData( 'C003', 'P079', 3 )
	data_mag.addPurchaseData( 'C014', 'P079', 3 )
	data_mag.addPurchaseData( 'C015', 'P079', 1 )
	data_mag.addPurchaseData( 'C019', 'P079', 3 )

	data_mag.addPurchaseData( 'C012', 'P080', 2 )
	data_mag.addPurchaseData( 'C013', 'P080', 3 )
	data_mag.addPurchaseData( 'C015', 'P080', 1 )
	data_mag.addPurchaseData( 'C016', 'P080', 2 )
	data_mag.addPurchaseData( 'C019', 'P080', 2 )

	data_mag.addPurchaseData( 'C002', 'P081', 3 )
	data_mag.addPurchaseData( 'C015', 'P081', 3 )
	data_mag.addPurchaseData( 'C019', 'P081', 4 )

	data_mag.addPurchaseData( 'C014', 'P082', 5 )
	data_mag.addPurchaseData( 'C016', 'P082', 5 )

	data_mag.addPurchaseData( 'C003', 'P083', 4 )
	data_mag.addPurchaseData( 'C015', 'P083', 3 )
	data_mag.addPurchaseData( 'C016', 'P083', 3 )

	data_mag.addPurchaseData( 'C013', 'P084', 2 )
	data_mag.addPurchaseData( 'C014', 'P084', 2 )
	data_mag.addPurchaseData( 'C015', 'P084', 3 )
	data_mag.addPurchaseData( 'C019', 'P084', 3 )

	data_mag.addPurchaseData( 'C002', 'P085', 2 )
	data_mag.addPurchaseData( 'C013', 'P085', 3 )
	data_mag.addPurchaseData( 'C015', 'P085', 4 )
	data_mag.addPurchaseData( 'C016', 'P085', 1 )

	data_mag.addPurchaseData( 'C003', 'P086', 3 )
	data_mag.addPurchaseData( 'C014', 'P086', 4 )
	data_mag.addPurchaseData( 'C019', 'P086', 3 )

	data_mag.addPurchaseData( 'C002', 'P087', 3 )
	data_mag.addPurchaseData( 'C013', 'P087', 3 )
	data_mag.addPurchaseData( 'C014', 'P087', 1 )
	data_mag.addPurchaseData( 'C019', 'P087', 3 )

	data_mag.addPurchaseData( 'C003', 'P088', 2 )
	data_mag.addPurchaseData( 'C014', 'P088', 3 )
	data_mag.addPurchaseData( 'C015', 'P088', 5 )

	data_mag.addPurchaseData( 'C012', 'P089', 3 )
	data_mag.addPurchaseData( 'C013', 'P089', 4 )
	data_mag.addPurchaseData( 'C015', 'P089', 3 )

	data_mag.addPurchaseData( 'C002', 'P090', 2 )
	data_mag.addPurchaseData( 'C003', 'P090', 2 )
	data_mag.addPurchaseData( 'C014', 'P090', 3 )
	data_mag.addPurchaseData( 'C015', 'P090', 3 )

	data_mag.addPurchaseData( 'C003', 'P091', 4 )
	data_mag.addPurchaseData( 'C012', 'P091', 3 )
	data_mag.addPurchaseData( 'C016', 'P091', 3 )

	data_mag.addPurchaseData( 'C002', 'P092', 2 )
	data_mag.addPurchaseData( 'C003', 'P092', 1 )
	data_mag.addPurchaseData( 'C013', 'P092', 3 )
	data_mag.addPurchaseData( 'C019', 'P092', 4 )


	# nhom D
	data_mag.addPurchaseData('C020', 'P012', 6)
	data_mag.addPurchaseData('C021', 'P012', 4)

	data_mag.addPurchaseData('C020', 'P013', 5)
	data_mag.addPurchaseData('C022', 'P013', 5)

	data_mag.addPurchaseData('C021', 'P014', 4)
	data_mag.addPurchaseData('C022', 'P014', 6)

	data_mag.addPurchaseData('C020', 'P015', 5)
	data_mag.addPurchaseData('C022', 'P015', 5)

	data_mag.addPurchaseData('C022', 'P016', 5)
	data_mag.addPurchaseData('C020', 'P016', 5)

	data_mag.addPurchaseData('C020', 'P017', 5)
	data_mag.addPurchaseData('C021', 'P017', 5)

	data_mag.addPurchaseData('C020', 'P018', 4)
	data_mag.addPurchaseData('C021', 'P018', 6)

	data_mag.addPurchaseData('C021', 'P019', 5)
	data_mag.addPurchaseData('C022', 'P019', 5)

	data_mag.addPurchaseData('C021', 'P020', 4)
	data_mag.addPurchaseData('C022', 'P020', 6)

	data_mag.addPurchaseData('C020', 'P021', 5)
	data_mag.addPurchaseData('C022', 'P021', 5)

	data_mag.addPurchaseData('C020', 'P022', 4)
	data_mag.addPurchaseData('C022', 'P022', 6)

	data_mag.addPurchaseData('C020', 'P023', 6)
	data_mag.addPurchaseData('C021', 'P023', 4)

	data_mag.addPurchaseData('C021', 'P024', 3)
	data_mag.addPurchaseData('C022', 'P024', 7)

	data_mag.addPurchaseData('C021', 'P025', 4)
	data_mag.addPurchaseData('C022', 'P025', 6)

	data_mag.addPurchaseData('C021', 'P026', 7)
	data_mag.addPurchaseData('C022', 'P026', 3)

	data_mag.addPurchaseData('C020', 'P027', 4)
	data_mag.addPurchaseData('C021', 'P027', 6)

	data_mag.addPurchaseData('C020', 'P028', 3)
	data_mag.addPurchaseData('C022', 'P028', 7)

	data_mag.addPurchaseData('C020', 'P029', 5)
	data_mag.addPurchaseData('C021', 'P029', 5)

	data_mag.addPurchaseData('C021', 'P030', 5)
	data_mag.addPurchaseData('C022', 'P030', 5)

	data_mag.addPurchaseData('C020', 'P031', 4)
	data_mag.addPurchaseData('C021', 'P031', 6)

	data_mag.addPurchaseData('C021', 'P032', 7)
	data_mag.addPurchaseData('C022', 'P032', 3)

	data_mag.addPurchaseData('C020', 'P033', 5)
	data_mag.addPurchaseData('C022', 'P033', 5)

	data_mag.addPurchaseData('C021', 'P034', 8)
	data_mag.addPurchaseData('C022', 'P034', 2)
	

	# nhom E
	data_mag.addPurchaseData('C023', 'P012', 1)
	data_mag.addPurchaseData('C024', 'P012', 4)
	data_mag.addPurchaseData('C025', 'P012', 3)
	data_mag.addPurchaseData('C027', 'P012', 2)

	data_mag.addPurchaseData('C023', 'P013', 2)
	data_mag.addPurchaseData('C024', 'P013', 3)
	data_mag.addPurchaseData('C026', 'P013', 2)
	data_mag.addPurchaseData('C027', 'P013', 3)

	data_mag.addPurchaseData('C025', 'P014', 3)
	data_mag.addPurchaseData('C024', 'P014', 4)
	data_mag.addPurchaseData('C026', 'P014', 3)

	data_mag.addPurchaseData('C023', 'P015', 3)
	data_mag.addPurchaseData('C027', 'P015', 3)
	data_mag.addPurchaseData('C026', 'P015', 4)

	data_mag.addPurchaseData('C023', 'P016', 1)
	data_mag.addPurchaseData('C024', 'P016', 2)
	data_mag.addPurchaseData('C025', 'P016', 2)
	data_mag.addPurchaseData('C026', 'P016', 2)
	data_mag.addPurchaseData('C027', 'P016', 3)

	data_mag.addPurchaseData('C026', 'P017', 3)
	data_mag.addPurchaseData('C023', 'P017', 2)
	data_mag.addPurchaseData('C025', 'P017', 5)

	data_mag.addPurchaseData('C023', 'P018', 4)
	data_mag.addPurchaseData('C024', 'P018', 2)
	data_mag.addPurchaseData('C026', 'P018', 3)
	data_mag.addPurchaseData('C027', 'P018', 1)

	data_mag.addPurchaseData('C025', 'P019', 2)
	data_mag.addPurchaseData('C026', 'P019', 3)
	data_mag.addPurchaseData('C027', 'P019', 5)

	data_mag.addPurchaseData('C024', 'P020', 4)
	data_mag.addPurchaseData('C027', 'P020', 3)
	data_mag.addPurchaseData('C026', 'P020', 3)

	data_mag.addPurchaseData('C023', 'P021', 1)
	data_mag.addPurchaseData('C024', 'P021', 2)
	data_mag.addPurchaseData('C025', 'P021', 3)
	data_mag.addPurchaseData('C026', 'P021', 2)
	data_mag.addPurchaseData('C027', 'P021', 2)

	data_mag.addPurchaseData('C024', 'P022', 5)
	data_mag.addPurchaseData('C023', 'P022', 3)
	data_mag.addPurchaseData('C027', 'P022', 2)

	data_mag.addPurchaseData('C025', 'P023', 3)
	data_mag.addPurchaseData('C026', 'P023', 4)
	data_mag.addPurchaseData('C024', 'P023', 3)

	data_mag.addPurchaseData('C023', 'P024', 2)
	data_mag.addPurchaseData('C027', 'P024', 3)
	data_mag.addPurchaseData('C024', 'P024', 2)
	data_mag.addPurchaseData('C026', 'P024', 1)
	data_mag.addPurchaseData('C025', 'P024', 2)

	data_mag.addPurchaseData('C025', 'P035', 3)
	data_mag.addPurchaseData('C026', 'P035', 2)
	data_mag.addPurchaseData('C024', 'P035', 5)

	data_mag.addPurchaseData('C023', 'P036', 2)
	data_mag.addPurchaseData('C027', 'P036', 3)
	data_mag.addPurchaseData('C024', 'P036', 2)
	data_mag.addPurchaseData('C026', 'P036', 1)
	data_mag.addPurchaseData('C025', 'P036', 2)

	data_mag.addPurchaseData('C025', 'P037', 2)
	data_mag.addPurchaseData('C027', 'P037', 1)
	data_mag.addPurchaseData('C026', 'P037', 1)
	data_mag.addPurchaseData('C023', 'P037', 2)
	data_mag.addPurchaseData('C024', 'P037', 4)

	data_mag.addPurchaseData('C027', 'P038', 2)
	data_mag.addPurchaseData('C025', 'P038', 2)
	data_mag.addPurchaseData('C023', 'P038', 2)
	data_mag.addPurchaseData('C026', 'P038', 4)

	data_mag.addPurchaseData('C024', 'P039', 2)
	data_mag.addPurchaseData('C023', 'P039', 2)
	data_mag.addPurchaseData('C027', 'P039', 3)
	data_mag.addPurchaseData('C026', 'P039', 3)

	data_mag.addPurchaseData('C023', 'P040', 3)
	data_mag.addPurchaseData('C026', 'P040', 2)
	data_mag.addPurchaseData('C024', 'P040', 5)

	data_mag.addPurchaseData('C025', 'P041', 2)
	data_mag.addPurchaseData('C023', 'P041', 2)
	data_mag.addPurchaseData('C026', 'P041', 2)
	data_mag.addPurchaseData('C024', 'P041', 4)

	data_mag.addPurchaseData('C023', 'P042', 4)
	data_mag.addPurchaseData('C027', 'P042', 6)

	data_mag.addPurchaseData('C024', 'P043', 3)
	data_mag.addPurchaseData('C023', 'P043', 2)
	data_mag.addPurchaseData('C025', 'P043', 2)
	data_mag.addPurchaseData('C026', 'P043', 3)

	data_mag.addPurchaseData('C027', 'P044', 2)
	data_mag.addPurchaseData('C024', 'P044', 4)
	data_mag.addPurchaseData('C023', 'P044', 2)
	data_mag.addPurchaseData('C025', 'P044', 2)

	data_mag.addPurchaseData('C026', 'P045', 3)
	data_mag.addPurchaseData('C024', 'P045', 2)
	data_mag.addPurchaseData('C025', 'P045', 3)
	data_mag.addPurchaseData('C027', 'P045', 2)

	data_mag.addPurchaseData('C023', 'P046', 2)
	data_mag.addPurchaseData('C027', 'P046', 3)
	data_mag.addPurchaseData('C026', 'P046', 2)
	data_mag.addPurchaseData('C025', 'P046', 3)

	data_mag.addPurchaseData('C024', 'P047', 3)
	data_mag.addPurchaseData('C026', 'P047', 2)
	data_mag.addPurchaseData('C023', 'P047', 2)
	data_mag.addPurchaseData('C027', 'P047', 3)

	data_mag.addPurchaseData('C025', 'P048', 2)
	data_mag.addPurchaseData('C023', 'P048', 2)
	data_mag.addPurchaseData('C024', 'P048', 3)
	data_mag.addPurchaseData('C026', 'P048', 3)

	data_mag.addPurchaseData('C027', 'P049', 4)
	data_mag.addPurchaseData('C025', 'P049', 2)
	data_mag.addPurchaseData('C026', 'P049', 2)
	data_mag.addPurchaseData('C023', 'P049', 2)

	data_mag.addPurchaseData('C024', 'P050', 2)
	data_mag.addPurchaseData('C027', 'P050', 3)
	data_mag.addPurchaseData('C026', 'P050', 3)
	data_mag.addPurchaseData('C025', 'P050', 2)

	data_mag.addPurchaseData('C023', 'P051', 5)
	data_mag.addPurchaseData('C024', 'P051', 3)
	data_mag.addPurchaseData('C026', 'P051', 2)


	
if __name__ == "__main__":
	main()