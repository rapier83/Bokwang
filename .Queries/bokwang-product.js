MasterSpec = [{
	"Unit": "Inch",
	"Manifold": {"Variables": ["Length", "Height", "Thickness","Depth", "Size", "Width"],
				 "Height": 1.50,
				 "Size": 0.75, 
				 "Depth": MasterSpec["Manifold"]["Size"]},
	"Fin": {"Height": MasterSpec["Height"] + 0.06,
			""
	},



}]

MasterSpec["Manifold"]["Length"] = MasterSpec["Manifold"]["width"] 



Finshields = [{
	"Name": { "Number": "2744",
			  "Prefix": "REL",
			  "Surfix": "G"},
	"Manifold": { "Height": 1.5,
				  "Length": 6.038
				  "NumberOfSlots": 13,
				  "FinSpacing": 0.509},
	"Fin": { "Length": 3.70,
			 "Height": 1.50,
			 "Thickness": 0.140},

}]

// Doubled! work!! MongoDB modeling and Django modeling!
// It's not boring but little bit bitter. Did I work twice?
// P.S Actually Including Workbench ERD, it's triple work~ jahahah