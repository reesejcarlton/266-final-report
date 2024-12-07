import json
import os
import pandas as pd

os.chdir('C:/Users/reese/OneDrive/Documents/MIDS/Fall 2024/DATASCI 266/Final/Data')
#%%
adele_songs = [
    # 19 (2008)
    "Daydreamer", "Best for Last", "Chasing Pavements", "Cold Shoulder", "Crazy for You",
    "Melt My Heart to Stone", "First Love", "Right as Rain", "Make You Feel My Love",
    "My Same", "Tired", "Hometown Glory",
    # 19 Bonus Tracks
    "Painting Pictures", "Now and Then", "That’s It, I Quit, I’m Movin’ On", "Many Shades of Black",
    # 21 (2011)
    "Rolling in the Deep", "Rumour Has It", "Turning Tables", "Don’t You Remember",
    "Set Fire to the Rain", "He Won’t Go", "Take It All", "I’ll Be Waiting",
    "One and Only", "Lovesong", "Someone Like You",
    # 21 Bonus Tracks
    "I Found a Boy", "If It Hadn’t Been for Love", "Hiding My Heart",
    # 25 (2015)
    "Hello", "Send My Love (To Your New Lover)", "I Miss You", "When We Were Young", "Remedy",
    "Water Under the Bridge", "River Lea", "Love in the Dark", "Million Years Ago",
    "All I Ask", "Sweetest Devotion",
    # 25 Bonus Tracks
    "Can’t Let Go", "Lay Me Down", "Why Do You Love Me",
    # 30 (2021)
    "Strangers By Nature", "Easy On Me", "My Little Love", "Cry Your Heart Out", "Oh My God",
    "Can I Get It", "I Drink Wine", "All Night Parking", "Woman Like Me", "Hold On",
    "To Be Loved", "Love Is a Game",
    # 30 Bonus Tracks
    "Wild Wild West", "Can’t Be Together", "Easy On Me (with Chris Stapleton)",
    # iTunes Live from SoHo (2009)
    "Crazy for You", "Right as Rain", "Make You Feel My Love", "Melt My Heart to Stone",
    "Hometown Glory", "Chasing Pavements", "Fool That I Am", "That’s It, I Quit, I’m Movin’ On",
    # iTunes Festival: London 2011 (2011)
    "One and Only", "Don’t You Remember", "Rumour Has It", "Take It All", "I Can’t Make You Love Me",
    "Rolling in the Deep",
    # Live at the Royal Albert Hall (2011)
    "Hometown Glory", "I’ll Be Waiting", "Don’t You Remember", "Turning Tables",
    "Set Fire to the Rain", "If It Hadn’t Been for Love", "My Same", "Take It All",
    "Rumour Has It", "Right as Rain", "One and Only", "Lovesong", "Chasing Pavements",
    "I Can’t Make You Love Me", "Make You Feel My Love", "Someone Like You", "Rolling in the Deep"
]


elvis_csv = pd.read_csv('elvis_songs.csv')
elvis_songs = list(elvis_csv['Column1'].iloc[1:])


johnny_songs = [
    "0-9",
    "The 20th Century Is Almost Over",
    "25 Minutes to Go",
    "706 Union",
    "A",
    "Abner Brown",
    "Accidentally on Purpose",
    "Adios Aloha",
    "Adulterous Woman",
    "After All",
    "After Taxes",
    "After the Ball",
    "Against the Wind",
    "Agony in Gethsemane",
    "Ah Bos Cee Dah",
    "Ain't Gonna Hobo No more",
    "Ain't Gonna Work Tomorrow",
    "Ain't No Grave",
    "Ain't You Ashamed",
    "All Around Cowboy",
    "All I Do Is Drive",
    "All Of God's Children Ain't Free",
    "All Over Again",
    "Allegheny",
    "Aloha Oe",
    "Always Alone",
    "Always on My Mind",
    "Amen",
    "American Remains",
    "American by Birth",
    "American Trilogy",
    "Ancient History",
    "And Now He's Alone",
    "Angel And the Badman",
    "Angel Band",
    "Angels Love Bad Men",
    "Another Broken Hearted Girl",
    "Another Man Done Gone",
    "Another Song to Sing",
    "Another Wide River to Cross",
    "Anthem '84",
    "Any Old Wind That Blows",
    "Apache Tears",
    "Appalachian Pride",
    "Are All the Children In",
    "Are You Washed In The Blood",
    "Arkansas Lovin' Man",
    "As Long as I Live",
    "As Long as The Grass Shall Grow",
    "Ascension Amen Chorus",
    "At Calvary",
    "At the Cross",
    "At the Wailing Wall",
    "Austin Prison",
    "Away in a Manger",
    "B",
    "(I'm Proud The) Baby Is Mine",
    "Baby Ride Easy",
    "Back In The Saddle Again",
    "A Backstage Pass",
    "Bad News",
    "Ballad Of A Teenage Queen",
    "The Ballad Of Annie Palmer",
    "The Ballad Of Barbara",
    "The Ballad Of Boot Hill",
    "The Ballad Of Forty Dollars",
    "The Ballad Of Jesse James",
    "The Ballad of Ira Hayes",
    "Ballad Of Little Fauss And Big Halsy",
    "Ballad Of The Ark",
    "Ballad Of The Harp Weaver",
    "Bandana",
    "The Banks Of The Ohio",
    "The Baron",
    "The Battle Of Nashville",
    "The Battle Of New Orleans",
    "Be Careful Who You Love (Arthur's Song)",
    "Beans For Breakfast",
    "The Beast In Me",
    "A Beautiful Day",
    "Beautiful Life",
    "Beautiful Memphis",
    "Beautiful Words",
    "Before My Time",
    "Begin West Movement",
    "Believe In Him",
    "A Believer Sings The Truth",
    "Belshazzar",
    "Ben Dewberry's Final Run",
    "Besser so, Jenny-Joe [Original German song]",
    "Best Friend",
    "Best of All Possible Worlds",
    "Better Class Of Losers",
    "Big Balls In Nashville",
    "The Big Battle",
    "Big Foot",
    "Big Iron",
    "The Big Light",
    "Big River",
    "Big Train (From Memphis)",
    "Bill's Theme",
    "Billy And Rex And Oral And Bob",
    "Billy Brown",
    "Bird On A Wire",
    "A Bird With A Broken Wing",
    "Blessed Are",
    "Blistered",
    "The Blizzard",
    "Blue Bandana",
    "Blue Christmas",
    "Blue Train",
    "Blueberry Hill",
    "Blues For Two",
    "The Blues Keep Gettin' Bluer",
    "Blue Yodel #1",
    "Blue Yodel #5",
    "Boa Constrictor",
    "Bonanza!",
    "Boogie",
    "Borderline (A Musical Whodunit)",
    "Born And Raised In Black And White",
    "Born To Lose",
    "Boss Jack",
    "Bottom Of A Mountain",
    "A Boy Named Sue",
    "Brakeman's Blues",
    "Brand New Dance",
    "Breaking Bread",
    "Bridge Over Troubled Water",
    "Broken Freedom Song",
    "Broken Hearted Lover",
    "Brown Eyes",
    "Brown-Eyed Handsome Man",
    "The Bug That Tried To Crawl Around The World",
    "Bull Rider",
    "Burden Of Freedom",
    "Bury Me Not On The Lone Prairie",
    "Busted",
    "C",
    "Cajun Born",
    "Calilou",
    "Call Daddy From The Mine(s)",
    "Call Me The Breeze",
    "Call Of The Wild",
    "Can't Help But Wonder Where I'm Bound",
    "Careless Love",
    "The Caretaker",
    "Casey",
    "Casey Jones",
    "Casey's Last Ride",
    "Cat's in the Cradle",
    "The Cattle Call",
    "'Cause I Love You",
    "A Ceiling, Four Walls, And A Floor",
    "A Certain Kinda Hurtin'",
    "Chain Gang",
    "Change The Locks",
    "Chattanooga City Limit Sign",
    "Chattanooga Sugarbabe",
    "The Chicken In Black",
    "Children",
    "Children, Go Where I Send Thee",
    "Choosing Of Twelve Disciples",
    "Christmas As I Knew It",
    "The Christmas Guest",
    "The Christmas Spirit",
    "Christmas Time's A Comin'",
    "Christmas With You",
    "(I'm Just An Old) Chunk Of Coal (But I'll Be A Diamond Someday)",
    "Church In The Wildwood",
    "Church Of The Holy Sepulchre",
    "Cindy",
    "Cindy, I Love You",
    "Cisco Clifton's Fillin' Station",
    "City Jail",
    "City Of New Orleans",
    "Class Of '55",
    "Clean Your Own Tables",
    "Clementine",
    "Close The Door Lightly",
    "Closer To The Bone",
    "Cloudburst",
    "Cocaine Blues",
    "Cocaine Carolina",
    "Cold Shoulder",
    "Cold, Cold Heart",
    "Cold, Lonesome Morning",
    "The Color Of Love",
    "Come Along And Ride This Train",
    "Come In, Stranger",
    "Come Take A Trip In My Airship",
    "Come To The Wailing Wall",
    "Come Unto Me",
    "Coming Home",
    "Committed To Parkview",
    "Concerning Your New Song",
    "The Continuance",
    "Cool Water",
    "Cotton Fields",
    "Cotton Pickin' Hands",
    "Country Boy",
    "Country Pie",
    "Country Trash",
    "The Cowboy Who Started The Fight",
    "The Cowboy's Prayer",
    "Cowboys And Ladies",
    "Crazy",
    "Crazy Old Soldier",
    "The Cremation of Sam McGee",
    "A Croft In Clachan (The Ballad Of Rob MacDunn)",
    "Crossing The Sea Of Galilee",
    "Crucifixion",
    "Cry! Cry! Cry!",
    "Crystal Chandeliers And Burgundy",
    "Cuban Soldier",
    "A Cup Of Coffee",
    "Custer",
    "D",
    "Daddy",
    "Daddy Sang Bass",
    "The Danger Zone",
    "Danny Boy",
    "Dark As A Dungeon",
    "Darling Am I The One",
    "Darlin' Companion",
    "Daughter Of A Railroad Man",
    "A Day In The Grand Canyon",
    "Dear Mrs.",
    "Death And Hell",
    "The Death Of Me",
    "Delia's Gone",
    "Deportee (Plane Wreck At Los Gatos)",
    "Desperado",
    "Desperados Waiting For A Train",
    "Destination Victoria Station",
    "Detroit City",
    "The Devil Comes Back to Georgia",
    "The Devil To Pay",
    "The Devil's Right Hand",
    "Diamonds In The Rough",
    "Didn't It Rain",
    "Dinosaur Song",
    "The Diplomat",
    "Dirty Old Egg-Suckin' Dog",
    "Do Lord",
    "Do What You Do, Do Well",
    "Doesn't Anybody Know My Name",
    "Doin' My Time",
    "Don't Go Near The Water",
    "Don't Make Me Go",
    "Don't Sell Daddy Any More Whiskey",
    "Don't Step On Mother's Roses",
    "Don't Take Anyone To Be Your Friend (Don't Take Everybody For Your Friend)",
    "Don't Take Your Guns To Town",
    "Don't Think Twice, It's Alright",
    "Dorraine Of Ponchartrain",
    "Down At Drippin' Springs",
    "Down In The Valley",
    "Down The Line",
    "Down The Road I Go",
    "Down The Street To 301",
    "Down There By The Train",
    "The Drifter",
    "Drink To Me Only With Thine Eyes",
    "Drive On",
    "Drums",
    "Duelin' Dukes",
    "E",
    "Earthquake And Darkness",
    "East Virginia Blues",
    "Easy Street",
    "Empty Chair",
    "The End Of Understanding",
    "Engine 143 (One-Forty-Three)",
    "The Engineer's Dying Child",
    "Even Cowgirls Get The Blues",
    "The Evening Train",
    "Everybody Loves A Nut",
    "Everybody's Trying To Be My Baby",
    "Everyone Gets Crazy",
    "Everything Is Beautiful",
    "F",
    "Face Of Despair",
    "Fair And Tender Ladies",
    "Fair Weather Friends",
    "Family Bible",
    "Far Away Places",
    "Far Side Banks Of Jordan",
    "Farmer's Almanac",
    "Farther Along",
    "Fast Boat to Sydney",
    "A Fast Song",
    "Father And Daughter (Father And Son)",
    "Feast Of The Passover",
    "Feeding The Multitude",
    "Field Of Diamonds",
    "Figgy Puddin'",
    "The First Noel",
    "First Time Ever I Saw Your Face",
    "Fisher's Of Men",
    "Five Feet High And Rising",
    "Five Minutes To Live",
    "Flesh And Blood",
    "The Flint Arrowhead",
    "Flushed From The Bathroom Of Your Heart",
    "Fly Little Bird",
    "The Folk Singer",
    "Folks Out On The Road",
    "Follow Me",
    "Follow Me Jesus",
    "Folsom Prison Blues",
    "Fools Hall Of Fame",
    "Foolish Questions",
    "For Lovin' Me",
    "For The Good Times",
    "For You",
    "Forever Young",
    "Forty Shades Of Green",
    "Four Months To Live",
    "Four Strong Winds",
    "The Fourth Man (In The Fire)",
    "Frankie's Man, Johnny",
    "Friendly Gates",
    "Friends In California",
    "From Sea To Shining Sea",
    "A Front Row Seat to Hear Ole Johnny Sing",
    "The Frozen Four Hundred Pound Fair To Middlin' Cotton Picker",
    "The Frozen Logger",
    "Fuego De'amor [Spanish version of Ring of Fire]",
    "Funny How Time Slips Away",
    "Further On (Up The Road)",
    "G",
    "Gadsby's Restaurant",
    "Galway Bay[1]",
    "The Gambler",
    "Gathering Flowers For The Beautiful Bouquet",
    "Gathering Flowers From The Hillside",
    "The General Lee",
    "Gentle On My Mind",
    "Georgia On A Fast Train",
    "Get in Line, Brother",
    "Get Rhythm",
    "The Gettysburg Address",
    "(Ghost) Riders In The Sky",
    "The Gifts They Gave",
    "Girl from the Canyon",
    "Girl from the North Country",
    "Girl in Saskatoon",
    "Give It Away",
    "Give Me Back My Job",
    "Give My Love To Rose",
    "Go On Blues",
    "Go Wild",
    "God Ain't No Stained Glass Window",
    "God Bless Robert E Lee",
    "God Is Not Dead",
    "God Must Have My Fortune Laid Away",
    "God Will",
    "God's Gonna Cut You Down",
    "God's Hands",
    "Godshine",
    "Goin' by the Book",
    "Goin' Down the Road Feelin' Bad",
    "Going to Memphis",
    "Gone",
    "Gone Girl",
    "The Good Earth",
    "Good Morning Friend",
    "Good Old American Guest",
    "Good Old Mountain Dew",
    "The Good, the Bad, and the Cookie Kid",
    "Goodbye Little Darlin'",
    "Goodnight Irene",
    "Gospel Boogie",
    "Gospel Road",
    "Gospel Ship",
    "(My) Grandfather's Clock[2]",
    "Great Commission",
    "The Great Speckle(d) Bird",
    "Greater Love Hath No Man",
    "The Greatest Cowboy of Them All",
    "Greatest Love Affair",
    "Green Grow the Lilacs",
    "Green, Green Grass of Home",
    "Greystone Chapel",
    "Guess Things Happen That Way",
    "H",
    "A Half a Mile a Day",
    "Hammers and Nails",
    "Hank and Joe and Me",
    "Happiness Is You",
    "Happy to Be with You",
    "Hard Times (Come Again No More)",
    "Hard Times Comin'",
    "The Hard Way",
    "Hardin Wouldn't Run",
    "Hark! The Herald Angels Sing",
    "Harley",
    "Have A Drink Of Water",
    "Have Thine Own Way Lord",
    "Have You Ever Seen the Rain",
    "He Is Risen",
    "He Stopped Loving Her Today",
    "He Touched Me",
    "He Turned The Water Into Wine",
    "He'll Be A Friend",
    "He'll Understand and Say Well Done",
    "He's Alive",
    "Heart Of Gold",
    "Heartbeat",
    "Heavy Metal (Don't Mean Rock And Roll To Me)",
    "Hello Again",
    "Hello Out There",
    "Help Him, Jesus",
    "Help Me",
    "Help Me Make It Through The Night",
    "Here Comes that Rainbow Again",
    "Here Was A Man",
    "Heroes",
    "Heroes In Black And White",
    "Hey Good Lookin'",
    "Hey Hey Train",
    "Hey, Porter",
    "Hiawatha's Vision",
    "Hidden Shame",
    "High Heel Sneakers",
    "Highway Patrolman",
    "The Highwayman",
    "Hit The Road And Go",
    "The Hobo Song",
    "Home of the Blues",
    "Honky Tonk Girl",
    "The House Is Falling Down",
    "How Beautiful Heaven Must Be",
    "How Did You Get Away From Me",
    "How Great Thou Art",
    "The Human Condition",
    "Hung My Head",
    "Hungry",
    "Hurt",
    "Hurt So Bad",
    "I",
    "I Ain't A Song",
    "I Am A Pilgrim",
    "I Am The Nation",
    "(I Been To) Georgia On A Fast Train",
    "I Call Him",
    "I Came To Believe",
    "I Can't Go On That Way",
    "I Can't Help It (If I'm Still In Love With You)",
    "I Corinthians 15:55",
    "I Could Never Be Ashamed Of You",
    "I Couldn't Keep from Crying",
    "I Do Believe",
    "I Don't Believe You Wanted To Leave",
    "I Don't Hurt Anymore",
    "I Don't Know Where I'm Bound",
    "I Don't Think I Could Take You Back Again",
    "I Dreamed About Mama Last Night",
    "I Drove Her Out of My Mind",
    "I Feel Better All Over",
    "I Forgot More Than You'll Ever Know",
    "I Forgot To Remember To Forget",
    "I Got A Boy (And His Name Is John)",
    "I Got a Woman",
    "I Got Shoes",
    "I Got Stripes",
    "I Hardly Ever Sing Beer Drinking Songs",
    "(I Heard That) Lonesome Whistle",
    "I Heard The Bells On Christmas Day",
    "I Hung My Head",
    "I Just Thought You'd Like To Know",
    "I Love You Because",
    "I Love You Sweetheart",
    "I Love You, Love You",
    "I Never Got To Know Him Very Well",
    "I Never Met A Man Like You Before",
    "I Never Picked Cotton",
    "I Promise You",
    "I Ride An Old Paint",
    "I Saw A Man",
    "I Saw The Light",
    "I See A Darkness",
    "I See Men As Trees Walking",
    "I Shall Be Free",
    "I Shall Not Be Moved",
    "I Still Miss Someone",
    "I Talk To Jesus Every Day",
    "I Threw It All Away",
    "I Tremble For You",
    "I Walk The Line",
    "I Want To Go Home",
    "I Wanted So",
    "I Was There When It Happened (So I Guess I Ought To Know)",
    "I Washed My Face In The Morning Dew",
    "I Will Dance With You",
    "I Will Miss You When You Go",
    "I Will Rock and Roll with You",
    "I Wish I Was Crazy Again",
    "I Witness a Crime",
    "I Won't Back Down (feat. Tom Petty)",
    "I Won't Have to Cross Jordan Alone",
    "I Would Like to See You Again",
    "I'd Just Be Fool Enough (To Fall)",
    "I'd Rather Die Young",
    "I'd Rather Have You",
    "I'd Still Be There",
    "I'll Always Love You (in My Own Crazy Way)",
    "I'll Be All Smiles Tonight",
    "I'll Be Home for Christmas",
    "I'll Be Loving You",
    "I'll Cross Over Jordon Someday",
    "I'll Fly Away",
    "I'll Go Somewhere And Sing My Songs Again",
    "I'll Have a New Life",
    "I'll Remember You",
    "I'll Say It's True",
    "I'll Take You Home Again Kathleen",
    "I'm A Drifter",
    "I'm A Newborn Man",
    "I'm A Worried Man",
    "I'm Alright Now",
    "I'm An Easy Rider",
    "I'm An Old Cow Hand",
    "I'm Bound For The Promised Land",
    "I'm Free From The Chain Gang Now",
    "I'm Going To Memphis",
    "I'm Gonna Sit On The Porch And Pick On My Old Guitar",
    "I'm Gonna Try To Be That Way",
    "I'm Here To Get My Baby Out Of Jail",
    "(I'm Just An Old) Chunk Of Coal (But I'll Be A Diamond Someday)",
    "I'm Leavin' Now",
    "I'm Movin' On",
    "I'm Never Gonna Roam Again",
    "I'm On Fire",
    "(I'm Proud) The Baby Is Mine",
    "I'm Ragged but I'm Right",
    "\"I'm So Lonesome I Could Cry\"",
    "I'm Thinking Tonight of My Blue Eyes",
    "I'm Working On A Building",
    "I've Always Been Crazy",
    "I've Been Everywhere",
    "I've Been Saved",
    "I've Been Working On The Railroad",
    "I've Got A Thing About Trains",
    "I've Got Jesus In My Soul",
    "I've Never Met A Man Like You Before",
    "If He Came Back Again",
    "If I Give My Soul",
    "If I Had A Hammer",
    "If I Were A Carpenter",
    "If It Wasn't For The Wabash River",
    "If Jesus Ever Loved A Woman",
    "If Not For Love",
    "If The Good Lord's Willing",
    "If We Never Meet Again This Side Of Heaven",
    "If You Could Read My Mind",
    "Impersonations",
    "Interlude",
    "In A Young Girl's Mind",
    "In Bethlehem",
    "In God's Hands",
    "In My Life",
    "In Our Mind",
    "In The Garden",
    "In The Garden Of Gethsemane",
    "In The Jailhouse Now",
    "In The Sweet By And By",
    "(In Them Old) Cotton Fields (Back Home)",
    "In Virginia [Original German song]",
    "In Your Mind",
    "Introduction Under The Double Eagle",
    "The Invertebrates",
    "Is This My Destiny",
    "It Ain't Gonna Worry My Mind",
    "It Ain't Me, Babe",
    "It Ain't Nothin' New Babe",
    "It Came Upon A Midnight Clear",
    "It Comes And Goes",
    "It Could Be You (Instead Of Him)",
    "It Is No Secret (What God Can Do)",
    "It Is What It Is",
    "It Takes One to Know Me",
    "It Was Jesus (Who Was It?)",
    "It'll Be Her",
    "It's a Sin to Tell a Lie",
    "It's All Over",
    "It's Alright",
    "It's Just About Time",
    "J",
    "Jackson",
    "Jacob Green",
    "Jealous Loving Heart",
    "Jeri And Nina's Melody",
    "Jesus",
    "Jesus and Children",
    "Jesus and Nicodemus",
    "Jesus Announces His Divinity",
    "Jesus Appears to Disciples",
    "Jesus Before Caiaphas, Pilate, and Herod",
    "Jesus Cleanses Temple",
    "Jesus Cleanses Temple Again",
    "Jesus In My Soul (I've Got Jesus in My Soul)",
    "Jesus in the Temple",
    "Jesus Is Lord",
    "Jesus Upbraids Scribes and Pharisees",
    "Jesus Was a Carpenter",
    "Jesus Was Our Saviour (Cotton Was Our King)",
    "Jesus Wept",
    "Jesus' Death",
    "Jesus' Early Years",
    "Jesus' Entry Into Jerusalem",
    "Jesus' First Miracle",
    "Jesus' Last Words",
    "Jesus' Opposition Is Established",
    "Jesus' Second Coming",
    "Jesus' Teachings",
    "Jim, I Wore a Tie Today",
    "Jingle Bells",
    "Joe Bean",
    "John 14-1-3",
    "John Henry",
    "John the Baptist",
    "John the Baptist's Imprisonment And Death",
    "John's",
    "Johnny 99",
    "Johnny Reb",
    "Jordan",
    "Joshua Gone Barbados",
    "Joy to the World",
    "The Junkie and the Juicehead (Minus Me)",
    "Just a Closer Walk with Thee",
    "Just About Time",
    "Just As I Am",
    "Just One More",
    "Just the Other Side of Nowhere",
    "K",
    "Kate",
    "Kathy",
    "Katy Too",
    "Keep on the Sunny Side",
    "Keep Your Eyes on Jesus",
    "Kentucky Straight",
    "King of Love",
    "King of The Hill",
    "Kleine Rosmarie [Original German song]",
    "The Kneeling Drunkard's Plea To",
    "The L and N Don't Stop Here Anymore",
    "Lady",
    "The Lady Came from Baltimore",
    "Land of Israel",
    "The Last Cowboy Song",
    "Last Date",
    "The Last Gunfighter Ballad",
    "Last Night I Had the Strangest Dream",
    "The Last of the Drifters",
    "Last Supper",
    "The Last Thing on my Mind",
    "The Last Time",
    "Lately",
    "Lately I Been Leanin' Toward The Blues",
    "Lay Back With My Woman",
    "Lay Me Down in Dixie",
    "Lead Me Father",
    "Lead Me Gently Home (Father)",
    "Leave That Junk Alone",
    "A Legend in My Time",
    "The Legend of John Henry's Hammer",
    "Let America Be America Again",
    "Let Him Roll",
    "Let Me Down Easy",
    "Let Me Help You Carry This Weight",
    "Let The Lower Lights Be Burning (Running)",
    "Let The Train Blow the Whistle",
    "Let There Be Country",
    "Let Those Brown Eyes Smile at Me",
    "The Letter Edged in Black",
    "Letter(s) From Home",
    "Life Goes On",
    "Life Has Its Little Ups and Downs",
    "Life of a Prisoner",
    "Life's Railway to Heaven",
    "Lights of Magdala",
    "Like a Soldier",
    "Like a Young Colt",
    "Like the 309",
    "The Lily of the Valley",
    "A Little at a Time",
    "Little Bit of Yesterday",
    "The Little Drummer Boy",
    "Little Gray Donkey",
    "Little Green Fountain",
    "Little Magic Glasses",
    "Little Man",
    "Little Mockingbird",
    "Live Forever",
    "Living Legend",
    "Living the Blues",
    "Living Water and the Bread of Life",
    "Loading Coal",
    "Locomotive Man",
    "Lonesome to the Bone",
    "Lonesome Valley",
    "(I Heard That) Lonesome Whistle (Blow)",
    "The Long Black Veil",
    "Long Legged Guitar Pickin' Man",
    "Look at Them Beans",
    "Look For Me",
    "Look Unto the East",
    "Lookin' Back in Anger",
    "Lord Is It I",
    "Lord Take These Hands",
    "Lord, I'm Coming Home",
    "Lord, Lord, Lord",
    "Lord's Prayer Amen Chorus",
    "Lorena",
    "Losin' You",
    "Losing Kind",
    "Lost on the Desert",
    "Louisiana Man",
    "Love Has Lost Again",
    "Love Is a Gambler",
    "Love Is My Refuge",
    "Love Is the Way",
    "Love Me Like You Used To",
    "Love Me Tender",
    "The Love That Never Failed",
    "Love's Been Good To Me",
    "Lovin' Locomotive Man",
    "The Loving Gift",
    "Lower Lights",
    "Lumberjack",
    "Luther Played The Boogie (Luther's Boogie)",
    "Mama, You've Been On My Mind",
    "Mama's Baby",
    "The Man Comes Around",
    "Man In Black",
    "Man In White",
    "The Man On The Hill",
    "The Man Who Couldn't Cry",
    "Mariners And Musicians",
    "Mary Magdalene Returns To Galilee",
    "Mary Of The Wild Moor",
    "The Masterpiece",
    "The Matador",
    "Matchbox",
    "Matthew 24 (Is Knocking At The Door)",
    "Me And Bobby McGee",
    "Me And Paul",
    "Mean As Hell",
    "Mean-Eyed Cat",
    "Meet Me In Heaven",
    "Melva's Wine",
    "Memories Are Made Of This",
    "Mercy Seat",
    "Merry Christmas Mary",
    "Michigan City Howdy Do",
    "Miller's Cave",
    "The Miracle Man",
    "Miss Tara",
    "Mississippi Delta Land",
    "Mississippi Sand",
    "Missouri Waltz",
    "Mister Garfield",
    "Mobile Bay",
    "Monteagle Mountain",
    "More Jesus Teaching",
    "Mother Maybelle",
    "Mother's Love",
    "Mountain Dew",
    "Mountain Lady",
    "Movin'",
    "Mr Garfield",
    "Mr Lonesome",
    "Muddy Waters",
    "My Children Walk In Truth",
    "My Clinch Mountain Home",
    "My Cowboy's Last Ride",
    "My God Is Real (Yes, God Is Real)",
    "(My) Grandfather's Clock",
    "My Merry Christmas Song",
    "My Mother Was A Lady",
    "My Old Faded Rose",
    "My Old Kentucky Home (Turpentine And Dandelion Wine)",
    "My Ship Will Sail",
    "My Shoes Keep Walking Back To You",
    "My Treasure",
    "My Wife June At Sea Of Galilee",
    "The Mystery Of Life",
    "Mystery Of Number Five",
    "Nashville Skyline Rag",
    "Nasty Dan",
    "Navajo",
    "Nazarene",
    "Ned Kelly",
    "Never Grow Old",
    "New Cut Road",
    "New Mexico",
    "New Moon Over Jamaica",
    "(I'm A) Newborn Man",
    "News Conference",
    "Next In Line",
    "Next Time I'm In Town",
    "The Night Hank Williams Came To Town",
    "Night Life",
    "The Night They Drove Old Dixie Down",
    "Nine Pound Hammer",
    "No Charge",
    "No Earthly Good",
    "No Expectations",
    "No Need To Worry",
    "No, No, No",
    "No One Will Ever Know",
    "No Setting Sun",
    "Nobody",
    "Nobody Cared",
    "O Christmas Tree",
    "O Come All Ye Faithful",
    "O Little Town Of Bethlehem",
    "Oh Bury Me Not On The Lone Prairie",
    "Oh Come, Angel Band",
    "Oh Lonesome Me",
    "Oh, What A Dream",
    "Oh, What A Good Thing We Had",
    "The Old Account Was Settled Long Ago",
    "Old Apache Squaw",
    "(I'm Just An) Old Chunk Of Coal (But I'll Be A Diamond Someday)",
    "Old Doc Brown",
    "Old Fashioned Tree",
    "Old Gospel Ship",
    "The Old Rugged Cross",
    "Old Shep",
    "The Old Spinning Wheel",
    "Old Time Feeling",
    "Ole Slew Foot",
    "On The Evening Train",
    "On The Line",
    "On The Road Again",
    "On The Trail",
    "On The Via Dolorosa",
    "On Wheels And Wings",
    "Once Before I Die",
    "One",
    "One And One Makes Two",
    "One More Ride",
    "One Of These Days I'm Gonna Sit Down And Talk To Paul",
    "The One On The Right Is On The Left",
    "One Piece At A Time",
    "The One Rose (That's Left In My Heart)",
    "One Too Many Mornings",
    "One Way Rider",
    "Oney",
    "Only Love",
    "Opening The West",
    "Orange Blossom Special",
    "Orleans Parish Prison",
    "Orphan Of The Road",
    "Our Guide Jacob At Mount Tabor",
    "Out Among The Stars",
    "Outside Looking In",
    "Over The Next Hill",
    "Over There",
    "Pack Up Your Sorrows",
    "Painted Desert",
    "Papa Was a Good Man",
    "Parable of the Good Shepherd",
    "Paradise",
    "Passin' Thru",
    "Paul Revere",
    "(There'll Be) Peace in the Valley (for Me)",
    "Peggy Day",
    "Personal Jesus",
    "Pick a Bale o' Cotton",
    "Pick the Wildwood Flower",
    "Pick Up the Tempo",
    "Pickin' Time",
    "Pie in the Sky",
    "The Pilgrim",
    "The Pine Tree",
    "Please Don't Let Me Out",
    "Please Don't Play Red River Valley",
    "Pocahontas",
    "Poor Valley Girl",
    "Port Of Lonely Hearts",
    "Praise The Lord And Pass The Soup",
    "The Preacher Said, \"Jesus Said\"",
    "Precious Memories",
    "The Prisoner's Song",
    "A Proud Land",
    "Put The Sugar To Bed",
    "R",
    "Ragged Old Flag",
    "Raising of Lazarus",
    "Reaching for the Stars",
    "Reason to Believe",
    "The Rebel – Johnny Yuma",
    "Red Velvet",
    "Redemption",
    "Redemption Day",
    "Redemption Song",
    "Reflections",
    "Relief Is Just A Swallow Away",
    "(Remember Me) I'm the One Who Loves You",
    "Remember The Alamo",
    "Restless",
    "Return To The Promised Land",
    "The Reverend Mr. Black",
    "Ride This Train",
    "(Ghost) Riders in the Sky",
    "Ridin' On The Cotton Belt",
    "Ring Of Fire",
    "Ringing The Bells For Jim",
    "Riot In Cell Block No 9",
    "The Road Goes On Forever",
    "The Road To Kaintuck",
    "Rock And Roll (Fais-Do-Do)",
    "Rock And Roll Ruby",
    "Rock And Roll Shoes",
    "Rock Island Line",
    "Rock Of Ages",
    "Rockabilly Blues (Texas 1955)",
    "Rocket 69",
    "Rodeo Hand",
    "Roll Call",
    "Rollin' Free",
    "Rosanna's Going Wild",
    "Rose Of My Heart",
    "Roughneck",
    "Route #1, Box 144",
    "Rowboat",
    "Run Softly, Blue River",
    "The Running Kind",
    "Rusty Cage",
    "S",
    "Saginaw, Michigan",
    "Sailor On A Concrete Sea",
    "Salty Dog",
    "Sam Hall",
    "Sam Stone",
    "San Quentin",
    "Sanctified",
    "A Satisfied Mind",
    "Saturday Night In Hickman County",
    "Sea of Heartbreak",
    "Seal It In My Heart And Mind",
    "Seasons Of My Heart",
    "Second Honeymoon",
    "See Ruby Fall",
    "Send A Picture Of Mother",
    "September When It Comes",
    "Sermon On The Mount",
    "Shamrock Doesn't Grow In California",
    "Shantytown",
    "She Came from the Mountains",
    "She's A Go-Er",
    "Shepherd Of My Heart",
    "The Shifting, Whispering Sands",
    "Shrimpin' Sailin'",
    "Silent Night",
    "(That) Silver Haired Daddy Of Mine",
    "Silver Stallion",
    "Sing A Song",
    "Sing A Travelin' Song",
    "Sing It Pretty, Sue",
    "A Singer Of Songs",
    "Singin' In Vietnam Talkin' Blues",
    "The Singing Star's Queen",
    "Single Girl, Married Girl",
    "Six Days On The Road",
    "Six Gun Shooting",
    "Six White Horses",
    "Sixteen Tons",
    "Slow Rider",
    "Smiling Bill McCall",
    "Smokey Factory Blues",
    "Snow In His Hair",
    "So Do I",
    "So Doggone Lonesome",
    "Softly And Tenderly",
    "Sold Out of Flagpoles",
    "Soldier Boy",
    "Soldier's Last Letter",
    "Solitary Man",
    "Someday My Ship Will Sail",
    "A Song For The Life",
    "Song Of The Coward",
    "Song Of The Patriot",
    "A Song To Mama",
    "Song To Woody",
    "Songs That Make A Difference",
    "The Sons Of Katie Elder",
    "The Sound Of Laughter",
    "Southern Accents",
    "Southern Comfort",
    "Southwestward",
    "Southwind",
    "Spanish Harlem",
    "Spiritual",
    "Stampede",
    "Standing on the Promises",
    "Starkville City Jail",
    "State of the Nation",
    "Steel Guitar Rag",
    "Still in Town",
    "The Story of a Broken Heart",
    "Straight A's in Love",
    "Strange Things Happen Every Day (There Are Strange Things Happening Every Day)",
    "Strawberry Cake",
    "The Streets Of Laredo",
    "Suffer Little Children",
    "Sugartime",
    "Sunday Mornin' Comin' Down",
    "Sunrise",
    "Sunset",
    "Suppertime",
    "Sweet Betsy from Pike",
    "Sweeter Than The Flowers",
    "Swing Low, Sweet Chariot",
    "T",
    "T Is For Texas",
    "Take Me Home",
    "The Talking Leaves",
    "Tall Man",
    "Taller Than Trees",
    "Tear Stained Letter",
    "Tears In The Holston River",
    "Tell Him I'm Gone",
    "Temptation",
    "The Ten Commandments",
    "The Ten Commandments Of Love",
    "Tennessee Flat-Top Box",
    "Tennessee Stud",
    "Texas",
    "Texas 1947",
    "Thanks A Lot",
    "Thanks To You",
    "That Christmasy Feeling",
    "That Lucky Old Sun (Just Rolls Around Heaven All Day)",
    "That Old Time Feeling",
    "That Old Wheel",
    "That Silver Haired Daddy Of Mine",
    "That's All Over",
    "That's Alright Mama",
    "That's Enough",
    "That's How I Got To Memphis",
    "That's One You Owe Me",
    "That's The Truth",
    "That's The Way It Is",
    "That's What It's Like To Be Lonesome",
    "There Ain't No Easy Run",
    "There Ain't No Good Chain Gang",
    "There Are Strange Things Happening Every Day",
    "There Is (There's) A Bear In The Woods",
    "There You Go",
    "(There'll Be) Peace In The Valley (For Me)",
    "These Are My People",
    "These Things Shall Pass",
    "They Killed Him",
    "They're All The Same",
    "A Thing Called Love",
    "Thirteen",
    "This Is Nazareth",
    "This Land Is Your Land",
    "This Ole House",
    "This Side Of The Law",
    "This Town",
    "This Train Is Bound For Glory",
    "Thoughts On The Flag",
    "The Three Bells",
    "Thunderball",
    "Tiger Whitehead",
    "The Timber Man",
    "Time And Time Again",
    "Time Changes Everything",
    "Time Of The Preacher",
    "To All The Girls I've Loved Before",
    "To Beat The Devil",
    "To The Shining Mountains",
    "Tonight I'll Be Staying Here With You",
    "Tony",
    "Too Little, Too Late",
    "Town Of Cana",
    "Train Of Love",
    "Transfusion Blues",
    "The Troubadour",
    "Trouble In Mind",
    "Troublesome Waters",
    "True Love Is Greater Than Friendship",
    "True Love Travels A Gravel Road",
    "The Twentieth Century Is Almost Over",
    "Two Greatest Commandments",
    "Two Old Army Pals",
    "Two Stories Wide",
    "Two Timin' Woman",
    "U",
    "Unchained",
    "Uncloudy Day",
    "Under The Double Eagle",
    "Understand Your Man",
    "Unwed Fathers",
    "V",
    "The Vanishing Race",
    "Vaya Con Dios",
    "The Very Biggest Circus Of Them All",
    "Veteran's Day",
    "Viel zu spät [German version of 'I Got Stripes']",
    "Virgien",
    "W. Lee O Daniel (And The Light Crust Dough Boys)",
    "Wabash Blues",
    "The Wabash Cannonball",
    "Waiting For A Long Time",
    "Waiting For A Southern Train",
    "Waiting For A Train",
    "Walkin' The Blues",
    "The Wall",
    "The Walls Of A Prison",
    "The Wanderer",
    "Walk the Line",
    "Wanted Man",
    "Water From The Wells Of Home",
    "Wayfaring Stranger",
    "Waymore's Blues",
    "The Ways Of A Woman In Love",
    "The Wayworn Traveler",
    "We Are The Shepherds",
    "We Must Believe In Magic",
    "We Ought To Be Ashamed",
    "We Remember The King",
    "We'll Meet Again",
    "We're All In Your Corner",
    "We're For Love",
    "Wednesday Car",
    "Welcome Back Jesus",
    "Welfare Line",
    "Wer kennt den Weg [German version of I Walk the Line]",
    "Were You There (When They Crucified My Lord)",
    "West Canterbury Subdivision Blues",
    "The West",
    "What Child Is This",
    "What Do I Care",
    "What Have You Got Planned Tonight, Diana",
    "What I've Learned",
    "What Is Man",
    "What Is Truth",
    "What On Earth (Will You Do For Heaven's Sake)",
    "What'd I Say",
    "What's Good For You (Should Be Alright For Me)",
    "When He Comes",
    "When He Reached Down His Hand For Me",
    "When I Look",
    "When I Stop Dreaming",
    "When I Take My Vacation In Heaven",
    "When I'm Gray",
    "When I've Learned (Enough To Die)",
    "When It's Springtime In Alaska (It's Forty Below)",
    "When Papa Played The Dobro",
    "(When) The Man Comes Around",
    "When The Roll Is Called Up Yonder",
    "When The Roses Bloom Again",
    "When The Saviour Reached Down For Me",
    "When Uncle Bill Quit Dope",
    "When You Are Twenty One",
    "Where Did We Go Right",
    "Where I Found You",
    "Where The Soul Of Man Never Dies",
    "Where We'll Never Grow Old",
    "While I've Got It On My Mind",
    "The Whirl And The Suck",
    "White Christmas",
    "White Girl",
    "Who At My Door Is Standing",
    "Who Kept The Sheep",
    "Who's Gene Autry?",
    "Why Do You Punish Me (For Loving You)",
    "Why Is A Fire Engine Red",
    "Why Me, Lord?",
    "Wichita Lineman",
    "Wide Open Road",
    "Wilderness Temptation",
    "Wildwood Flower",
    "Wildwood In The Pines",
    "Will The Circle Be Unbroken",
    "Will You Miss Me When I'm Gone",
    "The Wind Changes",
    "The Winding Stream",
    "Wings In The Morning",
    "Without Love",
    "Wo ist Zuhause, Mama [German version of Five Feet High and Rising]",
    "W-O-M-A-N",
    "The Wonder Of You",
    "A Wonderful Time Up There",
    "Woodcarver",
    "The World Needs A Melody",
    "World's Gonna Fall On You",
    "Worried Man",
    "Worried Man Blues",
    "Worried Mind",
    "Would You Lay with Me (In a Field of Stone)",
    "A Wound Time Can't Erase",
    "The Wreck Of The Old 97",
    "Wrinkled, Crinkled, Wadded Dollar Bill",
    "You And Me",
    "You And Tennessee",
    "You Are My Sunshine",
    "You Are (You're) The Nearest Thing To Heaven",
    "You Beat All I Ever Saw",
    "You Can't Beat Jesus Christ",
    "You Comb Her Hair",
    "You Dreamer You",
    "You Give Me Music",
    "You (Just) Can't Beat Jesus Christ",
    "You Remembered Me",
    "You Tell Me",
    "You Wild Colorado",
    "You Win Again",
    "You Won't Have Far to Go",
    "You'll Be All Right",
    "You'll Get Yours And I'll Get Mine",
    "You'll Never Walk Alone",
    "You're Driftin' Away",
    "You're Home Sweet Home To Me",
    "You're My Baby (Little Woolly Booger)",
    "You're So Close To Me",
    "You're The Nearest Thing To Heaven",
    "You've Got A New Light Shining In Your Eyes"
]

#%%
adele_file_path = 'Adele_songs_scraped_cleaned.json'

with open(adele_file_path, 'r') as file:
    adele_data = json.load(file)

adele_filtered_songs = [item for item in adele_data if item.get("title") in adele_songs]
with open('Adele_filtered_songs.json', 'w') as file:
    json.dump(adele_filtered_songs, file, indent=4)

#%%
elvis_file_path = 'Elvis_songs_scraped_cleaned.json'

with open(elvis_file_path, 'r') as file:
    elvis_data = json.load(file)

elvis_filtered_songs = [item for item in elvis_data if item.get("title") in elvis_songs]

with open('Elvis_filtered_songs.json', 'w') as file:
    json.dump(elvis_filtered_songs, file, indent=4)
#%%
johnny_file_path = 'Johnny_Cash_songs_scraped_cleaned.json'

with open(johnny_file_path, 'r') as file:
    johnny_data = json.load(file)

johnny_filtered_songs = [item for item in johnny_data if item.get("title") in johnny_songs]

with open('Johnny_filtered_songs.json', 'w') as file:
    json.dump(johnny_filtered_songs, file, indent=4)
#%%