"""
These dictionaries contain the naming convention used in Entso-e XTML files 
"""


ProcessTypeDict = {
"A01":"Day ahead",
"A02":"Intra day incremental",
"A16":"Realised",
"A18":"Intraday total",
"A31":"Week ahead",
"A32":"Month ahead",
"A33":"Year ahead",
"A39":"Synchronisation process",
"A40":"Intraday process",
"A46":"Replacement reserve",
"A47":"Manual frequency restoration reserve",
"A51":"Automatic frequency restoration reserve",
"A52":"Frequency containment reserve",
"A56":"Frequency restoration reserve"}


DocumentTypeDict = {
"A09":"Finalised schedule",
"A11":"Aggregated energy data report",
"A15":"Acquiring system operator reserve schedule",
"A24":"Bid document",
"A25":"Allocation result document",
"A26":"Capacity document",
"A31":"Agreed capacity",
"A38":"Reserve allocation result document",
"A44":"Price Document",
"A59":"Status request for a status within a process",
"A61":"Estimated Net Transfer Capacity",
"A63":"Redispatch notice",
"A65":"System total load",
"A68":"Installed generation per type",
"A69":"Wind and solar forecast",
"A70":"Load forecast margin",
"A71":"Generation forecast",
"A72":"Reservoir filling information",
"A73":"Actual generation",
"A74":"Wind and solar generation",
"A75":"Actual generation per type",
"A76":"Load unavailability",
"A77":"Production unavailability",
"A78":"Transmission unavailability",
"A79":"Offshore grid infrastructure unavailability",
"A80":"Generation unavailability",
"A81":"Contracted reserves",
"A82":"Accepted offers",
"A83":"Activated balancing quantities",
"A84":"Activated balancing prices",
"A85":"Imbalance prices",
"A86":"Imbalance volume",
"A87":"Financial situation",
"A88":"Cross border balancing",
"A89":"Contracted reserve prices",
"A90":"Interconnection network expansion",
"A91":"Counter trade notice",
"A92":"Congestion costs",
"A93":"DC link capacity",
"A94":"Non EU allocations",
"A95":"Configuration document",
"B11":"Flow-based allocations"}


#BZ — Bidding Zone

#BZA — Bidding Zone Aggregation

#CA — Control Area

#MBA — Market Balance Area

AreaDict={
"10YDE-VE-------2":"50Hertz CA, DE(50HzT) BZA",
"10YAL-KESH-----5":"Albania, OST BZ / CA / MBA",
"10YDE-RWENET---I":"Amprion CA",
"10YAT-APG------L":"Austria, APG CA / MBA",
"BY":"Belarus",
"10Y1001A1001A51S":"Belarus BZ / CA / MBA",
"10YBE----------2":"Belgium, Elia BZ / CA / MBA",
"10YBA-JPCC-----D":"Bosnia Herzegovina, NOS BiH BZ / CA / MBA",
"10YCA-BULGARIA-R":"Bulgaria, ESO BZ / CA / MBA",
"10YDOM-CZ-DE-SKK":"BZ CZ+DE+SK BZ / BZA",
"10YHR-HEP------M":"Croatia, HOPS BZ / CA / MBA",
"10YDOM-REGION-1V":"CWE Region",
"10YCY-1001A0003J":"Cyprus, Cyprus TSO BZ / CA / MBA",
"10YCZ-CEPS-----N":"Czech Republic, CEPS BZ / CA/ MBA",
"10Y1001A1001A63L":"DE-AT-LU BZ",
"10Y1001A1001A82H":"DE-LU MBA",
"10Y1001A1001A65H":"Denmark",
"10YDK-1--------W":"DK1 BZ / MBA",
"10YDK-2--------M":"DK2 BZ / MBA",
"10Y1001A1001A796":"Denmark, Energinet CA",
"10Y1001A1001A39I":"Estonia, Elering BZ / CA / MBA",
"10YFI-1--------U":"Finland, Fingrid BZ / CA / MBA",
"10YMK-MEPSO----8":"Former Yugoslav Republic of Macedonia, MEPSO BZ / CA / MBA",
"10YFR-RTE------C":"France, RTE BZ / CA / MBA",
"10Y1001A1001A83F":"Germany",
"10YGR-HTSO-----Y":"Greece, IPTO BZ / CA/ MBA",
"10YHU-MAVIR----U":"Hungary, MAVIR CA / BZ / MBA",
"IS":"Iceland",
"10Y1001A1001A59C":"Ireland (SEM) BZ / MBA",
"10YIE-1001A00010":"Ireland, EirGrid CA",
"10YIT-GRTN-----B":"Italy, IT CA / MBA",
"10Y1001A1001A885":"Italy_Saco_AC",
"10Y1001A1001A893":"Italy_Saco_DC",
"10Y1001A1001A699":"IT-Brindisi BZ",
"10Y1001A1001A70O":"IT-Centre-North BZ",
"10Y1001A1001A71M":"IT-Centre-South BZ",
"10Y1001A1001A72K":"IT-Foggia BZ",
"10Y1001A1001A66F":"IT-GR BZ",
"10Y1001A1001A84D":"IT-MACROZONE NORTH MBA",
"10Y1001A1001A85B":"IT-MACROZONE SOUTH MBA",
"10Y1001A1001A877":"IT-Malta BZ",
"10Y1001A1001A73I":"IT-North BZ",
"10Y1001A1001A80L":"IT-North-AT BZ",
"10Y1001A1001A68B":"IT-North-CH BZ",
"10Y1001A1001A81J":"IT-North-FR BZ",
"10Y1001A1001A67D":"IT-North-SI BZ",
"10Y1001A1001A76C":"IT-Priolo BZ",
"10Y1001A1001A77A":"IT-Rossano BZ",
"10Y1001A1001A74G":"IT-Sardinia BZ",
"10Y1001A1001A75E":"IT-Sicily BZ",
"10Y1001A1001A788":"IT-South BZ",
"10Y1001A1001A50U":"Kaliningrad BZ / CA / MBA",
"10YLV-1001A00074":"Latvia, AST BZ / CA / MBA",
"10YLT-1001A0008Q":"Lithuania, Litgrid BZ / CA / MBA",
"10YLU-CEGEDEL-NQ":"Luxembourg, CREOS CA",
"10Y1001A1001A93C":"Malta, Malta BZ / CA / MBA",
"10YCS-CG-TSO---S":"Montenegro, CGES BZ / CA / MBA",
"10YGB----------A":"National Grid BZ / CA/ MBA",
"GB":"Great Britain CTY",
"10YNL----------L":"Netherlands, TenneT NL BZ / CA/ MBA",
"10YNO-1--------2":"NO1 BZ / MBA",
"10YNO-2--------T":"NO2 BZ / MBA",
"10YNO-3--------J":"NO3 BZ / MBA",
"10YNO-4--------9":"NO4 BZ / MBA",
"10Y1001A1001A48H":"NO5 BZ / MBA",
"10YNO-0--------C":"Norway, Norway MBA, Stattnet CA",
"10YDOM-1001A082L":"PL-CZ BZA / CA",
"10YPL-AREA-----S":"Poland, PSE SA BZ / BZA / CA / MBA",
"10YPT-REN------W":"Portugal, REN BZ / CA / MBA",
"10Y1001A1001A990":"Republic of Moldova, Moldelectica BZ/CA/MBA",
"10YRO-TEL------P":"Romania, Transelectrica BZ / CA/ MBA",
"10Y1001A1001A49F":"Russia BZ / CA / MBA",
"RU":"Russian Federation",
"10Y1001A1001A44P":"SE1 BZ / MBA",
"10Y1001A1001A45N":"SE2 BZ / MBA",
"10Y1001A1001A46L":"SE3 BZ / MBA",
"10Y1001A1001A47J":"E4 BZ / MBA",
"10YCS-SERBIATSOV":"Serbia, EMS BZ / CA / MBA",
"10YSK-SEPS-----K":"Slovakia, SEPS BZ / CA / MBA",
"10YSI-ELES-----O":"Slovenia, ELES BZ / CA / MBA",
"10Y1001A1001A016":"Northern Ireland, SONI CA",
"10YES-REE------0":"Spain, REE BZ / CA / MBA",
"10YSE-1--------K":"Sweden, Sweden MBA, SvK CA",
"10YCH-SWISSGRIDZ":"Switzerland, Swissgrid BZ / CA / MBA",
"10YDE-EON------1":"TenneT GER CA",
"10YDE-ENBW-----N":"TransnetBW CA",
"TR":"Turkey",
"10YTR-TEIAS----W":"Turkey BZ / CA / MBA",
"10Y1001C--00003F":"Ukraine, Ukraine BZ, MBA",
"10Y1001A1001A869":"Ukraine-DobTPP CTA",
"10YUA-WEPS-----0":"Ukraine BEI CTA",
"10Y1001C--000182":"Ukraine IPS CTA"}

#A.5. PsrType

PsrTypeDict = {
"A03":"Mixed",
"A04":"Generation",
"A05":"Load",
"B01":"Biomass",
"B02":"Fossil Brown coal/Lignite",
"B03":"Fossil Coal-derived gas",
"B04":"Fossil Gas",
"B05":"Fossil Hard coal",
"B06":"Fossil Oil",
"B07":"Fossil Oil shale",
"B08":"Fossil Peat",
"B09":"Geothermal",
"B10":"Hydro Pumped Storage",
"B11":"Hydro Run-of-river and poundage",
"B12":"Hydro Water Reservoir",
"B13":"Marine",
"B14":"Nuclear",
"B15":"Other renewable",
"B16":"Solar",
"B17":"Waste",
"B18":"Wind Offshore",
"B19":"Wind Onshore",
"B20":"Other",
"B21":"AC Link",
"B22":"DC Link",
"B23":"Substation",
"B24":"Transformer"}