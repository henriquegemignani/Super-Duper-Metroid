# This file will hold data specific to Super Metroid which both the patcher and the interface use.
# This file only holds constants - any data specific to a given patch or version is not present.

class SuperMetroidConstants:
    # List of ammo items, ordered by ascending Message ID
    ammoItemList = [
        "Energy Tank",
        "Missile Expansion",
        "Super Missile Expansion",
        "Power Bomb Expansion",
        "Reserve Tank"
    ]
    
    # List of toggle items, ordered by ascending Message ID
    toggleItemList = [
        "Grapple Beam",
        "X-Ray Scope",
        "Varia Suit",
        "Spring Ball",
        "Morph Ball",
        "Screw Attack",
        "Hi-Jump Boots",
        "Space Jump",
        "Speed Booster",
        "Charge Beam",
        "Ice Beam",
        "Wave Beam",
        "Spazer Beam",
        "Plasma Beam",
        "Morph Ball Bombs",
        "Gravity Suit"
    ]
    
    # Combined list, in order of ascending Message ID
    itemList = ammoItemList[0:4] + toggleItemList[0:15] + [ammoItemList[4]] + [toggleItemList[15]]
    
    # Dictionary of nonstandard message box sizes
    # TODO: Replace this with something more elegant? Possibly.
    itemMessageNonstandardSizes = {
        "Missile Expansion"       : "0100",
        "Super Missile Expansion" : "0100",
        "Power Bomb Expansion"    : "0100",
        "Morph Ball Bombs"        : "0100",
        "Speed Booster"           : "0100",
        "Grapple Beam"            : "0100",
        "X-Ray Scope"             : "0100"}
    
    # Dictionary of item message locations
    itemMessageAddresses = {
        "Energy Tank"             : "877F",
        "Missile Expansion"       : "87BF",
        "Super Missile Expansion" : "88BF",
        "Power Bomb Expansion"    : "89BF",
        "Grapple Beam"            : "8ABF",
        "X-Ray Scope"             : "8BBF",
        "Varia Suit"              : "8CBF",
        "Spring Ball"             : "8CFF",
        "Morph Ball"              : "8D3F",
        "Screw Attack"            : "8D7F",
        "Hi-Jump Boots"           : "8DBF",
        "Space Jump"              : "8DFF",
        "Speed Booster"           : "8E3F",
        "Charge Beam"             : "8F3F",
        "Ice Beam"                : "8F7F",
        "Wave Beam"               : "8FBF",
        "Spazer Beam"             : "8FFF",
        "Plasma Beam"             : "903F",
        "Morph Ball Bombs"        : "907F",
        "Reserve Tank"            : "94FF",
        "Gravity Suit"            : "953F"}
    
    itemMessageIDs = {
        "Energy Tank"             : "0001",
        "Missile Expansion"       : "0002",
        "Super Missile Expansion" : "0003",
        "Power Bomb Expansion"    : "0004",
        "Grapple Beam"            : "0005",
        "X-Ray Scope"             : "0006",
        "Varia Suit"              : "0007",
        "Spring Ball"             : "0008",
        "Morph Ball"              : "0009",
        "Screw Attack"            : "000A",
        "Hi-Jump Boots"           : "000B",
        "Space Jump"              : "000C",
        "Speed Booster"           : "000D",
        "Charge Beam"             : "000E",
        "Ice Beam"                : "000F",
        "Wave Beam"               : "0010",
        "Spazer Beam"             : "0011",
        "Plasma Beam"             : "0012",
        "Morph Ball Bombs"        : "0013",
        "Reserve Tank"            : "0019",
        "Gravity Suit"            : "001A"}
    
    # Widths for all messages, either "Small" or "Large".
    # Small boxes have a width of 19 tiles,
    # Large boxes have a width of 26 tiles.
    # This dictates how messages are generated.
    # If a message type is not in this dict,
    # It is "Small".
    # All non-item messages, such as save station menus, recharge stations, etc. are also always small.
    # This includes unused messages.
    # Note that messageboxes may have varying heights.
    itemMessageWidths = {
        "Energy Tank"             : "Small",
        "Missile Expansion"       : "Large",
        "Super Missile Expansion" : "Large",
        "Power Bomb Expansion"    : "Large",
        "Grapple Beam"            : "Large",
        "X-Ray Scope"             : "Large",
        "Varia Suit"              : "Small",
        "Spring Ball"             : "Small",
        "Morph Ball"              : "Small",
        "Screw Attack"            : "Small",
        "Hi-Jump Boots"           : "Small",
        "Space Jump"              : "Small",
        "Speed Booster"           : "Large",
        "Charge Beam"             : "Small",
        "Ice Beam"                : "Small",
        "Wave Beam"               : "Small",
        "Spazer Beam"             : "Small",
        "Plasma Beam"             : "Small",
        "Morph Ball Bombs"        : "Large",
        "Reserve Tank"            : "Small",
        "Gravity Suit"            : "Small"}
    
    itemPLMIDs = {
        "Energy Tank"             : "EED7",
        "Missile Expansion"       : "EEDB",
        "Super Missile Expansion" : "EEDF",
        "Power Bomb Expansion"    : "EEE3",
        "Morph Ball Bombs"        : "EEE7",
        "Charge Beam"             : "EEEB",
        "Ice Beam"                : "EEEF",
        "Hi-Jump Boots"           : "EEF3",
        "Speed Booster"           : "EEF7",
        "Wave Beam"               : "EEFB",
        "Spazer Beam"             : "EEFF",
        "Spring Ball"             : "EF03",
        "Varia Suit"              : "EF07",
        "Gravity Suit"            : "EF0B",
        "X-Ray Scope"             : "EF0F",
        "Plasma Beam"             : "EF13",
        "Grapple Beam"            : "EF17",
        "Space Jump"              : "EF1B",
        "Screw Attack"            : "EF1F",
        "Morph Ball"              : "EF23",
        "Reserve Tank"            : "EF27",
        # This will replace the item with nothing at all.
        # Its space will simply be empty, nothing will be there.
        # This is NOT the same as the "No Item" routine, which is
        # Attached to an actual item, but simply does nothing when picked up
        # To affect the player's current gamestate.
        "No Item"                 : "B62F"}
    
    # List of all possible item locations as they are ordered in memory.
    # This looks really good if you have a monospace font.
    # If you don't have one you're a chump.
    itemLocationList = [
        "00", "01", "02", "03", "04", "05", "06", "07",
        "08", "09", "0A", "0B", "0C", "0D", "0E", "0F",
        "10", "11", "12", "13",       "15", "16", "17",
        "18", "19", "1A", "1B", "1C", "1D", "1E", "1F",
              "21", "22", "23", "24", "25", "26", "27",
        "28", "29", "2A", "2B", "2C",
        "30", "31", "32", "33", "34", "35", "36", "37",
        "38", "39", "3A", "3B", "3C", "3D", "3E", "3F",
        "40", "41", "42", "43", "44",       "46", "47",
              "49", "4A", "4B", "4C", "4D", "4E", "4F",
        "50",

        "80", "81", "82", "83", "84", "85", "86", "87",
        "88", "89", "8A", "8B", "8C", "8D", "8E", "8F",
        "90", "91", "92", "93", "94", "95", "96", "97",
        "98",       "9A"]
    
    # List of item PLM type offsets.
    # Used to set items as shot block or chozo orbs when necessary,
    # Depending upon which location an item is placed into.
    itemPLMBlockTypeList = [
        0, 0, 2, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 0, 1, 1, 0,
        0, 1, 2, 0,    0, 0, 1,
        0, 0, 0, 0, 0, 2, 0, 0,
           0, 1, 0, 0, 2, 1, 0,
        1, 0, 1, 2, 2,
        1, 2, 1, 2, 0, 1, 0, 0,
        0, 0, 0, 0, 1, 1, 2, 0,
        0, 2, 1, 0, 1,    0, 2,
           0, 0, 0, 0, 0, 2, 1,
        0,

        0, 1, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 2, 0, 0, 0, 1,
        0, 1, 0, 0, 0, 0, 1, 2,
        0,       1]
    
    # List of item PLM Locations in ROM.
    # This is where we place each item's entity so that it will show up in the room.
    # Doing so overwrites the item that would have been there previously (i.e. in an unpatched ROM).
    itemPLMLocationList = [
        "781CC", "781E8", "781EE", "781F4", "78248", "78264", "783EE", "78404",
        "78432", "78464", "7846A", "78478", "78486", "784AC", "784E4", "78518",
        "7851E", "7852C", "78532", "78538",          "78608", "7860E", "78614",
        "7865E", "78676", "786DE", "7874C", "78798", "7879E", "787C2", "787D0",
                 "787FA", "78802", "78824", "78836", "7883C", "78876", "788CA",
        "7890E", "78914", "7896E", "7899C", "789EC",             
        "78ACA", "78AE4", "78B24", "78B46", "78BA4", "78BAC", "78BC0", "78BE6",
        "78BEC", "78C04", "78C14", "78C2A", "78C36", "78C3E", "78C44", "78C52",
        "78C66", "78C74", "78C82", "78CBC", "78CCA",          "78E6E", "78E74",
                 "78F30", "78FCA", "78FD2", "790C0", "79100", "79108", "79110",
        
        "79184",
        "7C265", "7C2E9", "7C2EF", "7C319", "7C337", "7C357", "7C365", "7C36D",
        "7C437", "7C43D", "7C47D", "7C483", "7C4AF", "7C4B5", "7C533", "7C559",
        "7C5DD", "7C5E3", "7C5EB", "7C5F1", "7C603", "7C609", "7C6E5", "7C74D",
        "7C755",          "7C7A7"]
    
    locationNamesList = [
        "Crateria Landing Site Power Bombs",
        "Crateria Ocean Underwater Missiles",
        "Crateria Ocean Cliff Missiles",
        "Crateria Ocean Morph Maze Missiles",
        "Crateria Moat Missiles",
        "Crateria Gauntlet Energy Tank",
        "Crateria Mother Brain Missiles",
        "Crateria Morph Ball Bombs",
        
        "Crateria Terminator Energy Tank",
        "Crateria Gauntlet Right Missiles",
        "Crateria Gauntlet Left Missiles",
        "Crateria Shinespark Shaft Super Missiles",
        "Crateria Final Missiles",
        "Green Brinstar Etecoons Power Bombs",
        "Pink Brinstar Spore Spawn Super Missiles",
        "Green Brinstar Early Supers Crumble Bridge Missiles",
        
        "Green Brinstar Early Supers Super Missiles",
        "Green Brinstar Reserve Tank",
        "Green Brinstar Reserve Tank Missiles 2",
        "Green Brinstar Reserve Tank Missiles",
        "Pink Brinstar Big Pink Grapple Missiles",
        "Pink Brinstar Big Pink Bottom Missiles",
        "Pink Brinstar Charge Beam",
        
        "Pink Brinstar Big Pink Grapple Power Bombs",
        "Green Brinstar Green Hill Zone Missiles",
        "Blue Brinstar Morph Ball",
        "Blue Brinstar Power Bombs",
        "Blue Brinstar Energy Tank Room Missiles",
        "Blue Brinstar Energy Tank",
        "Green Brinstar Etecoons Energy Tank",
        "Green Brinstar Etecoons Super Missiles",
        
        "Pink Brinstar Waterway Energy Tank",
        "Blue Brinstar First Missiles",
        "Pink Brinstar Wavegate Energy Tank",
        "Blue Brinstar Billy Mayes Missiles",
        "Blue Brinstar Billy Mayes' Double Offer Missiles",
        "Red Brinstar X-Ray Scope",
        "Red Brinstar Samus Eater Power Bombs",
        
        "Red Brinstar Alpha Power Bombs",
        "Red Brinstar Behind Alpha Power Bombs Missiles",
        "Red Brinstar Spazer",
        "Warehouse Brinstar Energy Tank",
        "Warehouse Brinstar Missiles",
        
        "Warehouse Brinstar Varia Suit",
        "Norfair Cathedral Missiles",
        "Norfair Ice Beam",
        "Norfair Crumble Shaft Missiles",
        "Norfair Crocomire Energy Tank",
        "Norfair Hi-Jump Boots",
        "Norfair Crocomire Escape Missiles",
        "Norfair Hi-Jump Missiles",
        
        "Norfair Hi-Jump Energy Tank",
        "Norfair Crocomire Power Bombs",
        "Norfair Crocomire Cosine Missiles",
        "Norfair Grapple Missiles",
        "Norfair Grapple Beam",
        "Norfair Bubble Mountain Reserve Tank",
        "Norfair Bubble Mountain Reserve Missiles",
        "Norfair Bubble Mountain Grapple Missiles",
        
        "Norfair Bubble Mountain Missiles",
        "Norfair Speedboost Missiles",
        "Norfair Speed Booster",
        "Norfair Wave Beam Missiles",
        "Norfair Wave Beam",
        "Norfair Golden Torizo Missiles",
        "Norfair Golden Torizo Super Missiles",
        
        "Norfair Mickey Mouse Missiles",
        "Norfair Springball Maze Missiles",
        "Norfair Lower Escape Power Bombs",
        "Norfair Power Bombs of Shame",
        "Norfair FrankerZ Missiles",
        "Norfair Ridley Energy Tank",
        "Norfair Screw Attack",
        
        "Norfair Dark Room Energy Tank",
        
        "Wrecked Ship Spooky Missiles",
        "Wrecked Ship Reserve Tank",
        "Wrecked Ship Bowling Missiles",
        "Wrecked Ship Robot Missiles",
        "Wrecked Ship Energy Tank",
        "Wrecked Ship West Super Missiles",
        "Wrecked Ship East Super Missiles",
        "Wrecked Ship Gravity Suit",
        
        "Maridia Main Street Missiles",
        "Maridia Main Street Super Missiles",
        "Maridia Turtle Energy Tank",
        "Maridia Turtle Missiles",
        "Maridia Watering Hole Super Missiles",
        "Maridia Watering Hole Missiles",
        "Maridia Pseudo-Spark Missiles",
        "Maridia Plasma Beam",
        
        "Maridia West Sandtrap Missiles",
        "Maridia Reserve Tank",
        "Maridia East Sandtrap Missiles",
        "Maridia East Sandtrap Power Bombs",
        "Maridia Aqueduct Missiles",
        "Maridia Aqeuduct Super Misiles",
        "Maridia Springball",
        "Maridia Precious Missiles",
        
        "Maridia Botwoon Energy Tank",
        "Maridia Space Jump"]
    
    regionToHexDict = {
        "Crateria"     : "0000",
        "Brinstar"     : "0100",
        "Norfair"      : "0200",
        "Wrecked Ship" : "0300",
        "Maridia"      : "0400",
        "Tourian"      : "0500"
        
    }
    
    itemNameToQuantityName = {
        "Energy Tank"             : "Energy",
        "Missile Expansion"       : "Missiles",
        "Super Missile Expansion" : "Super Missiles",
        "Power Bomb Expansion"    : "Power Bombs",
        "Reserve Tank"            : "Reserve Energy"
    }
    
    defaultAmmoItemToQuantity = {
        "Energy Tank"             : 100,
        "Missile Expansion"       : 5,
        "Super Missile Expansion" : 5,
        "Power Bomb Expansion"    : 5,
        "Reserve Tank"            : 100
    }
    
    # Address to current quantity of indicated type.
    # Max quantity is stored 2 bytes after current quantity in all cases.
    ammoItemAddresses = {
        "Energy Tank"             : "F509C2",
        "Missile Expansion"       : "F509C6",
        "Super Missile Expansion" : "F509CA",
        "Power Bomb Expansion"    : "F509CE",
        "Reserve Tank"            : "F509D4"
    }
    
    # What address we should look at to find equipment (from SNI's perspective, it's complicated)
    toggleItemBaseAddress = "F509A2"
    
    # Formatted offsets for where to read/write toggleable items.
    # Stored as a tuple.
    # First  value: Byte offset.
    # Second value: Bit offset.
    # NOTE: Equipped and collected items are stored adjacently in memory.
    # The item collected flag is always exactly two bytes after the corresponding item equipped flag.
    # Bit offset is the offset from lsb.
    # Ex. the 1 in 00000001 has offset 0.
    toggleItemBitflagOffsets = {
        "Grapple Beam"     : (1, 6),
        "X-Ray Scope"      : (1, 7),
        "Varia Suit"       : (0, 0),
        "Spring Ball"      : (0, 1),
        "Morph Ball"       : (0, 2),
        "Screw Attack"     : (0, 3),
        "Hi-Jump Boots"    : (1, 0),
        "Space Jump"       : (1, 1),
        "Speed Booster"    : (1, 5),
        "Charge Beam"      : (5, 4),
        "Ice Beam"         : (4, 1),
        "Wave Beam"        : (4, 0),
        "Spazer Beam"      : (4, 2),
        "Plasma Beam"      : (4, 3),
        "Morph Ball Bombs" : (1, 4),
        "Gravity Suit"     : (0, 5)
    }
    
    vanillaPickupList = [
        "Power Bomb Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Energy Tank",
        "Missile Expansion",
        "Morph Ball Bombs",
        
        "Energy Tank",
        "Missile Expansion",
        "Missile Expansion",
        "Super Missile Expansion",
        "Missile Expansion",
        "Power Bomb Expansion",
        "Super Missile Expansion",
        "Missile Expansion",
        
        "Super Missile Expansion",
        "Reserve Tank",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Charge Beam",
        
        "Power Bomb Expansion",
        "Missile Expansion",
        "Morph Ball",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Energy Tank",
        "Energy Tank",
        "Super Missile Expansion",
        
        "Energy Tank",
        "Missile Expansion",
        "Energy Tank",
        "Missile Expansion",
        "Missile Expansion",
        "X-Ray Scope",
        "Power Bomb Expansion",
        
        "Power Bomb Expansion",
        "Missile Expansion",
        "Spazer Beam",
        "Energy Tank",
        "Missile Expansion",
        
        "Varia Suit",
        "Missile Expansion",
        "Ice Beam",
        "Missile Expansion",
        "Energy Tank",
        "Hi-Jump Boots",
        "Missile Expansion",
        "Missile Expansion",
        
        "Energy Tank",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Grapple Beam",
        "Reserve Tank",
        "Missile Expansion",
        "Missile Expansion",
        
        "Missile Expansion",
        "Missile Expansion",
        "Speed Booster",
        "Missile Expansion",
        "Wave Beam",
        "Missile Expansion",
        "Super Missile Expansion",
        
        "Missile Expansion",
        "Missile Expansion",
        "Power Bomb Expansion",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Energy Tank",
        "Screw Attack",
        
        "Missile Expansion",
        
        "Missile Expansion",
        "Reserve Tank",
        "Missile Expansion",
        "Missile Expansion",
        "Energy Tank",
        "Super Missile Expansion",
        "Super Missile Expansion",
        "Gravity Suit",
        
        "Missile Expansion",
        "Super Missile Expansion",
        "Energy Tank",
        "Missile Expansion",
        "Super Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Plasma Beam",
        
        "Missile Expansion",
        "Reserve Tank",
        "Missile Expansion",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Super Missile Expansion",
        "Spring Ball",
        "Missile Expansion",
        
        "Energy Tank",
        "Space Jump"]
    
    
    
        