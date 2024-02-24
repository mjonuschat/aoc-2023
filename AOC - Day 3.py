#!/usr/bin/env python
# coding: utf-8

# In[26]:


INPUT = """
.........874.772...........787..........556.....292......141................910............54...............................................
.......*..*.......314............308.......*....*..............156.759.....*................*.......408*954.84..55.......................515
......927.49...........734...............115...738..=....723..........*...599.......+........573.....................324..../508............
........................*.....222..................298....+........313.............504...../.....375.................................114....
.962...262............988..........*170.....................543...........61............827..244.&..................610......310....#.......
...*..........129...............243...................809....&...+.........*...742............%....*96..100.....766...*..308....*......37...
..2...295....../........*336..*......#..185...........*.........502......301...*.......................*...........-.770..-...599...........
.......-.............343......750..661....%........+..323.....1..............480.........+..............198.......................533.../764
..................................................799.....832.......640.................413...392............597.................=..........
......$795...678....954.....*96...........671.%..........*.......23....@.536..................*...450..........*.....427..............413...
..314...........*.....+.827.......757.550*.....475.148.614.........@......$.......*429.....849....*...%584....706....*..........248...*.....
.......246.......830....*..........................*.......52..................663...............55...............606........%.......72.....
......&.....378.........342....10.849............394.....&...*.....697*............................./629...700........=.......217...........
........208*......*783.........*...*.......496.........108...757..............564..............................904....448...................
..../..........716............428..28..879*..........................*506.823....*690......53...................*.............291......357..
..920.@172.........869..................................185.......809......../.............*......*821.......296..............*.......*.....
...........965........*...................669.793........................*................238..609......465.........504.....574..970=.575...
...................520.....................*.....&......................2.44..*......*..............@...*.......254*.....17.................
............574../.......*..............894...........939....236...875........92..873....555.825*.543..344..483......677*......123..........
...257..../.*....301.....83......*929........+.......&.............*...=...#..............#...................................*.............
.......218...648...../.....................533.683*....419........76.461.268......915...............523.....482.............788........845..
..................846......405.807.................693....%...................668*....193$....*......*.....@.......368.67..........703*.....
................&.............*.........752.988......................967*..................652.746.772...6........*.........................
....638.....769.829....*...97......536.#..........................&......786......@......................*......440.........................
....*........*..........55...*......*...............598*387.......744..........141....254*......157.....977..32...................606.392...
...682........268............134...187.........25.........................................561.....*............*.................*......*...
.......718........773............................*.....781...380......856....445......601.......71..........884........949*13..888.......277
.......*......487*.......$....$........8..@613....868.....*.....&....*............899*....*994........116............................806....
....807.............441..848.692.-13...*...................723........646.....525...........................*............289...........*.957
........-......891.....@.............185........672............................*.....626..937............838............@...........698.....
....634..418.....@.......75.430................*.......588-....815..56*685....714...@....*........+................385*.....................
620..*.......720....580........*521.772...222..763.888...........*........../..........537.818..534....................370..942.384...991...
.....462.......*...&.......118......*....................915.....797......255.....734........*.................*.............=.....-....*...
...............529..........+..701#..56.......@447..@......%..........-..............=.....197..../..........37....223.................186..
............#......................................702.846...........791..85..698..............755......458........#........847.............
.........993......916...@669.....493.........&...........*.....*..........*..-...........921...........$...............100...*..717.....489.
..................-................*.456..634.........202....=.815.......769................*...................300.....#..649...*......*...
....................762................*........211.......164.........27............817.286.....@493..............*............@..422.837...
......470.............*...............160...........560.......962.....*.....431.909..*..*...712.........852....838.........64.614...........
........*........404...406.=561....98........@........-.195.....*...320..........*..922.777..*.............%.&.........530..................
.71.....680.-79.....*..............*..859....625...............300..............465....................515...795...111.....646@.............
...................13...545.....386....*...............................865..........537.815........731.*.............*..........=.572*......
...........173.......................324...............................*...../.......*.....*157......*.480........175...662$..471.....136...
.....443*6...*...........*165....481............211/...373*297........470.....982..402............895........54.............................
...........11...&.....848...........@..........................@769.......................120...................555*........%........734....
..............827..........723...........178.............308........659............#492......*.............10.......80.......966.....*......
.....438-........................$.........................$./......*....%196..............299...393......*..............78.........629.....
.......................743....200...............243..702......447....775.........328.......................274.......360*.......459.........
....723..........514..../...........479......76*......*.........../......&....../......861...........$807......................*......+.....
.......*.....987................226....*.........#..867..........481......165......415*...................212...%649.....923-...685....346..
...+....914...*...........336.....@.278..622....204......269.976........................487.....%...727-.*..................................
..937.........38..-......$.................-........992.......*................628..740*.....%.445........360..............429.......917....
..........$.......592........481*285.....=.................126.............................269.......702........................823.#.......
..........593..52........546.............282..*226..............108..412.............=............#..................869....@....&..........
628............*..768......=.655...................*............*.....*...../..909....855....$....400.......238.........*11..545............
.............577....................../......147....945.31......979.846....403../.............742............*.......=.............#........
505+................485.............411......-..........-...........................536...-.........144......885....42...218.147...329......
......................&.849*714..........94*...856..........89..457.......*.....%...&...180........*......@..............*......*...........
....................-.......................68........651../...........264...&..252...............359...256..669*.......766..668...193......
.........992....743.860..174....&303............883.....*.....732..........433..........609...125................308.................*......
..592....#...64..*..........*........656..505..*......546.....&........422.........#............*.613.382..123............%....721...572....
...*.........*..........839.364.........*....*.549..............336...*...........129.......632....*....*.....#..647..122..25...............
.612...-..%............$..............628..489......................-.850..633.........=......*...972.660........*....*.....................
.....410..765.........................................../102.652..529.....*.............533..788............449&..8..875...846..392..649....
....................&.......581.....352............107+..................251.....130........................................./.......$......
.....807.........722...........*....*..........#...............+.116...............+..122.................184*491..&142.....................
.....&....755............894..227.315.........648..968......515....&.................*.....+..62............................................
............*.............-...........523............*....-...........165......434...106.427....#............241...........461......451.....
...#246...905.297..#668......=.....=....$...........712..778..968........*........*...............592........*.......703#..............*....
..............*............837....396........898..............+.....232.110....785...............*.........644...803...................178..
.......&190....69...*665....................*...................161.&.................618.../.........660..........*............850.........
.............$.............896.896.........884.............287...#........568................588.........@.........236....369$.....&........
.....@........464.........$....*............................*......958....*.......816.......................................................
..385.................877............160........263...&763..634...-........556.....*....658......953.......276........634+..&...........861.
......................*.....914.208.*..............*................472....................@........*937.#....*745..........841..910...-....
.......851........259..339.....*.....756.........285................*.........-................66+.......111........................@.......
.409....@........*.........................474.........+...197......180.@.....567.......................................850.................
....*......972.739.....*.....831*.............=......489.................611............*246.....................27.......*..631#......+....
.....314...*........334.968......739......505...............844.......................................732..............322...........33.....
............49...&..........*...............*........791..........152.....................247....166.............243.........826............
529&..544........275.....140.322..........73......+......435...................942...273....*.......#........749....*.......*...............
........*.......................................665.....*..................562....@........114.170-............/..92.........443..........51
......534.............212..........385................306.....863.....357....&........717...............570#................................
..............783.......*...........*..........................@...@.*............593*....*249....*338.............804..#...496.............
...=..........*......373....../570.65................../...836.....1..685....*39.......584................938........&.642....*..865..40#...
.715...909..142...........................136....892..192...@.............121...............629..........$.................651..............
................147........-....758..........=...*.............+...89.........678...815.997....*.....................990....................
...........*90.*....777.....868...*.............909.........361.....&..354....*...........+..200.....438.......62...*........521............
...............840...&..144.....861.....................479.............*...+...........................&.....*.....682......#........950...
....456.237................*................................146.......927..917..858....601..................834........................$....
.......*.....794...661.....618................369...#.......&....&................*.....*.....753.................381/.....*397..........524
.415................*.............490+.......*......533...........766..=.......657.......511...=........................766.................
...............539@.50..164...............583...574......409............126........34...................%652........44........%......886....
...907...................*..................................*346.............359.....*.........&.887...............*........115.837.=.......
......*...............3.666.............................736.........208.226..-......616.....250.......859..628....829.............*....+600.
......153..262.........................947......260......*.........*......*............................*...*..../...............93.../......
..........*..........421.................$.........%..500..107......402.264...407.....703..49..........54..424..372..684...........147.249..
......363..942...137*.....197..............*83............*...................*......*....*...158.......................-....73........*....
.........+...............*..........116..32............*...900..............360....479....54.........435*192.@850...........*...........325.
..390*..............=..431...518......*......436.......892.......787.517................%.......18.....................625.95....582........
......600...-176..415.......=.........780.......*...........*702..*..*.....699..........914.........186.......49*897..............*..558....
......................312........................40......481.........872.#....$./198..........764...+............................352........
.............800.........*.248.............571..................14........845............627.....*.......*...............336.664............
.........910.......395.506....*.........@..&.............567...*..............573..913....*......334..*..759......29.%.....&....+...........
..328.......*399.....*...........180...936....97$..376...*......251.....#447...............304.......450.....226.=...408..............*.....
......479............259........*...................*....78.........848......568......305..................=.*.............917..542.667.....
......#......332.............785.........422......624.63...........@.....896.@.........+..=770...530.....630..641.............*.........292.
............*..............................-.@..........*...$.............*......&..%..........%............................832..534...#....
.....560...400......................246*......411.....377...645.........62......620..465....146................#.986..185........*..........
......*.........761*......323@..........466...........................................................-111..382....*.....*.......408...164..
.......247.....................575*..........................836.496*380..125...321...............841...........648.....976............@....
.254.......74-.....+.......926.......-....844*.........224................*......*......562..811../...226...................................
...*..............162.*261.....287....758.....638........+.....479........834...80............=...........................188........287....
...734....396...................*.............................*.....406.*.............244#..............&....320.............*.*165.$.......
..........*..........31......221.......$384............*115.308.87..../..306....88#....................230...@............768...............
........694......441*............53..............35.814.........-.......................77......379.....................&..........-........
..................................*............-.+.......527......975...........594*......*........*857.#37..........302...........947..716.
.......104*561......978.226....925...........244.....107.........*..................336...749.............................691...........*...
..654..........561+...*....&.......54....924........=.........385..238........661*...............49......=.......456.859+...$.........479...
...*......392.........587....-....*.........*.965.....863.........&.....801.......19..$......*.....*529.881..670*.................790.......
.615.....-........570.....11.547.166.....347...*..190*.....................=...........302...236...........................&................
.....................*686.....................43..........79...........475......396.......................................610..#856.........
..................+...............$......................*...592.........*.....*.........804.......@30......629...23........................
...............202..954..%..958..894....503..579........904..*.....573..603.....450......*...734.........56....&..&.....415......408.511&...
.........750.........*..454....*......%..../..$..747#.......493......=......455.......252...*.....999.....................*........*........
...239...*........180.........594......280............412*.............255.....*..........17..338...........950..228.......840..809.........
........572.............326......................518.........................700.............*........263......*....@.675*............22....
...182....................*......................*......85...731...@.........................130.........*........*.......408....727@.+.....
...*....110....$899..+...755...568.=309........192.......*...*...259.847...557*42.......*........304/.....608....351........................
...823.+.............765......../........-508.........516...412.......*..............704...............................275.........210......
...........356........................#..........439......*........564....372*...846.............=........+62....-........*..298......*964..
.......%......*...308.....-4.........420......./..*....905.551..........$..........#.452*........417.195..........276...956.....*...$.......
....996.......413.....569.....#.810..........889..328..........*.........595.............359..........+..%.......................35.416.....
551......$...............*..357....*....627.............94..784.719..........697*76..........135..735....690.........944*177................
.......711............770...........664...=.......#...../...............730*..........58....*.......*...........182............848..........
...*........800................#..............#....929......=843............216.........*...412....473...735....*.....610*.....*...505......
348.5.......*......317......920................224...............503..-158.............463..............*.......865.......674.750.....@.....
.......367.723......*...................42.........636............+............$599..........948.......882..............................173.
.........&........873........=...........*...........*....292..-..............................*......................597*923................
..............................871.......497..........159........452.................900...116..450...878...........................302...574
"""


# In[87]:


import re
def day3_puzzle1():
    part_numbers = []
    schematic = INPUT.strip().splitlines()
    max_row = len(schematic) -1
    for row, line in enumerate(schematic):
        for m in re.finditer(r"(?P<part_num>\d+)", line):
            if m.start() > 0 and line[m.start() - 1] != ".":
                part_numbers.append(int(m.group('part_num')))
                continue
            if m.end() < len(line)-1 and line[m.end()] != ".":
                part_numbers.append(int(m.group('part_num')))
                continue

            if row > 0:
                symbols = schematic[row-1][max(0,m.start()-1):m.end()+1]
                if symbols.replace('.', ''):
                    part_numbers.append(int(m.group('part_num')))
                    continue
                    
            if row != max_row:
                symbols = schematic[row+1][max(0,m.start()-1):m.end()+1]
                if symbols.replace('.', ''):
                    part_numbers.append(int(m.group('part_num')))

    print(f"Sum of part_numbers: {sum(part_numbers)}")
    
def day3_puzzle2():
    gears = []
    symbols = []
    ratios = []
    schematic = INPUT.strip().splitlines()
    for row, line in enumerate(schematic):
        for m in re.finditer(r"(?P<ratio>\d+)", line):
            gears.append((m.start(), row, m.group('ratio')))
            
    for row, line in enumerate(schematic):
        for m in re.finditer(r"(?P<symbol>\*)", line):
            symbols.append((m.start(), row))

    for sx,sy in symbols:
        neighbors = []
        for x, y, r in gears:
            if not (sy-1 <= y <= sy+1):
                continue
            if x-1 <= sx <= x+len(r):
                neighbors.append((x,y,r))

        if len(neighbors) == 2:
            ratios.append(int(neighbors[0][2])*int(neighbors[1][2]))

    print(f"Sum of gear ratios: {sum(ratios)}")

    
day3_puzzle1()
day3_puzzle2()


# In[ ]:




