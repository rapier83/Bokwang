
// Mark : - 필드의 특정값 조회 후 변경

	holders = db.Companies.distinct('Bank') // return unique value of the field('Bank')

	db.Companies.find ({ Bank:holders[i] })

	db.Companies.find({ Bank:"기업" }).forEach(
		function(s){print(s._id)}
		);

	// return '_id' only 기업'
	db.BankList.find({ NameFull:{ $regex:"기업" }}, { _id:1 });

// Mark : - Update Basic Method
	// cur.insert({})
	cur.update(
		{ /* query: { field: value } */ }, 
		{ $set: { /* field Name */: { /* or $ operand */: /* value */ }}}, 
		{ upsert: /* boolean */, multi: /* boolean */ },
	);


// Scheme: - Payments.Company

	// Ver 0.01
	{
		_id: ObjectId("5b0c067c2db25d48243390d3"),
		"Name": "㈜마이크로컴택"
		"Bank": "기업"
		"AccountNumber": "270-052447-04016"
	}


	cur = db.Companies // Set cursor

	// Ver 0.89
	updateScheme =
		{ $set: {
			"RegistrationNumber":"",
			"Street1": "",
			"Street2": "",
			"City": "",
			"Province": "",
			"Country": 0,
			"CEOName": "",
			"CreditCardAblity": false,
			"Phone1": "",
			"Phone2": "",
			"FAX": "",
			"E-Mail":"",
			}
		}

	cur.update(updateScheme)

	// Ver 0.9 : - Add 'EnglishName' field to all documents
		// Basic Method
		cur.update( 
			{ /* query: all document (SELECT * ...) */ }, 
			{ $set: {"EnglishName": "" }}, 
			{ upsert:true, multi:true }
		);
		// Update Scheme to 0.9 Ver
		cur.update( {}, {$rename: {
				'Street2': 'Address.Street2', // sub-collection is `Address`
				'Street1': 'Address.Street1',
				'Street2': 'Address.Street2',
				'City': 'Address.City',
				'Province': 'Address.Province',
				'Country': 'Address.Country',
			}},
			{
				upsert: true,
				multi: true
			}
		);

// Mark: - Query a companie's by account bank

db.BankList.findOne(
	{ NameFull: { $regex:"기업" }})._id


// Scheme: - Product Management

	ProductManagement = {
		"OrderFrom": ObjectID(),
		"isAccept": boolean,
		"Order": Orders
		"MatrialCheck": 

	}

// Scheme: - Purchasing Order

	PurchaseOrders = [{
		DocumentInfos: {
			OrderFrom: "Owens Corning Composites(China) Co.,Ltd",
			PONumber: 4580342444,
			ContractPerson: ["ShenkeYing", ""],
			Tel: "+86 571 8936 1066",
			Fax: "+86 571 8936 1102",
			PODate: Date(2017, 4, 25)
		},
		DeliveriesInfo: { 
			ItemsTo: "",
			InvoceTo: "",
			DeliveryDate:Date(2017,5,12)
		},
		Items: { 
			Item: "00010",
			Material:"824523",
			ItemName: "",
			Quantity: 600,
			Unit: "EA",
			UnitPrice: 7.000001,
			Currency: "USD",
			VATRate: 0.00001,
			Description:"BLADE, FINS, 5, 13*1.5*0.14INCH,5800H"
		},
		isAcknowledgement: true,
	}]
		
	
		

// Scheme: - Products.ItemInfo

Products.ItemInfo =	{ $set: {
		"_id": ObjectID("5b30ce543ea0e94fe0cfb341"),
		"Name": "REL1150B",
		"UnitPrice": 190000,
		"Sort": 0,
		"Product Number": 0,
		"Product Type": 0,
		"DetailShape": "B",
		"isExported": true ,
		"Specification": {
			"Size": { "height": 0.1,
					  "Width": 0.1,
					  "Depth": 0.1,
					  "Unit": "Inches",
					  },
			"Blades": { "Number of Pins": 13,
						  "Height": 0.1,
						  "Width": 0.1,
						  "Angle": [2.2 ,2.2 ,2.2 ,0.1 ,0.3 ,0.4 ,0.5 ,0.4 ,0.6 ,0.2 , 0.3 , 1.1 , 0 , 1],
			              "Unit": "degree" 
						}
			
			"Manifold": { "Height": 0.1, 
						"Width": 0.1,
					  }
		}
	}
}
			

Process = [{
	"_id": ObjectId("5b3afdd4b524ed05e0e872e0"),
	"Order": ObjectId("5b3afde2b524ed05e0e872e1"),
	"Expected": Date(2018, 1, 1),
	"Completed": Date(2018, 1, 2),
	"Holling": {
		"isInclued": true,
		"Expected": Date(2018, 1, 1),
		"Completed": Date(2018, 1, 2)
	},
	"Rugging": {
		"isInclued": true,
		"Expected": Date(2018, 1, 1),
		"Completed": Date(2018, 1, 2)
	},
	"Filling": {
		"isInclued": true,
		"Expected": Date(2018, 1, 1),
		"Completed": Date(2018, 1, 2)
	},
	"Blading": {
		"isInclued": true,
		"Expected": Date(2018, 1, 1),
		"Completed": Date(2018, 1, 2)
	},
	"Sanding": {
		"isInclued": true,
		"Expected": Date(2018, 1, 1),
		"Completed": Date(2018, 1, 2)
	},
	"Coating": {
		"isInclued": true,
		"Expected": Date(2018, 1, 1),
		"Completed": Date(2018, 1, 2)
	},
	"Packing": {
		"isInclued": true,
		"Expected": Date(2018, 1, 1),
		"Completed": Date(2018, 1, 2)
	}
}]
	