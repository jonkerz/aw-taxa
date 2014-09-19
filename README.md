
Python script used to generate a wiki formatted list of ant genera/species from [AntWeb's](http://www.antweb.org/) catalog.

### Download
    .....

### Requirements
    pip install -r requirements.txt
    
or
    
    pip install beautifulsoup4==4.3.2
    pip install requests==2.4.1
    pip install argparse==1.2.1
    
### Usage
    usage: aw_species.py [-h] [-s] [-a] [-d] [-f FILE] taxon

    positional arguments:
        taxon                 subfamily or genus, not case sensitive

    optional arguments:
        -h, --help            show this help message and exit
        -s, --subspecies      include subspecies, default=False
        -a, --author-citations
                            include author citations, default=True
        -d, --debug           debug mode, default=False
        -f FILE, --file FILE  input file, default=null

### Example output
$python aw_taxa.py acromyrmex
    taxon = Acromyrmex
    include_author_citations = True
    include_subspecies = False
    url = http://www.antweb.org/browse.do?rank=genus&genus=acromyrmex&project=worldants

    Downloading page...
    http://www.antweb.org/browse.do?rank=genus&genus=acromyrmex&project=worldants downloaded successfully

    Parsing HTML...

    ==Species==
    {{div col|2}}
    *''[[Acromyrmex ambiguus]]'' <small>(Emery, 1888)</small>
    *''[[Acromyrmex ameliae]]'' <small>De Souza, Soares & Della Lucia, 2007</small>
    *''[[Acromyrmex aspersus]]'' <small>(Smith, 1858)</small>
    *''[[Acromyrmex balzani]]'' <small>(Emery, 1890)</small>
    *''[[Acromyrmex biscutatus]]'' <small>(Fabricius, 1775)</small>
    *''[[Acromyrmex coronatus]]'' <small>(Fabricius, 1804)</small>
    *''[[Acromyrmex crassispinus]]'' <small>(Forel, 1909)</small>
    *''[[Acromyrmex diasi]]'' <small>Gonçalves, 1983</small>
    *''[[Acromyrmex disciger]]'' <small>(Mayr, 1887)</small>
    *''[[Acromyrmex echinatior]]'' <small>(Forel, 1899)</small>
    *''[[Acromyrmex evenkul]]'' <small>Bolton, 1995</small>
    *''[[Acromyrmex fracticornis]]'' <small>(Forel, 1909)</small>
    *''[[Acromyrmex heyeri]]'' <small>(Forel, 1899)</small>
    *''[[Acromyrmex hispidus]]'' <small>Santschi, 1925</small>
    *''[[Acromyrmex hystrix]]'' <small>(Latreille, 1802)</small>
    *''[[Acromyrmex insinuator]]'' <small>Schultz, Bekkevold & Boomsma, 1998</small>
    *''[[Acromyrmex landolti]]'' <small>(Forel, 1885)</small>
    *''[[Acromyrmex laticeps]]'' <small>(Emery, 1905)</small>
    *''[[Acromyrmex lobicornis]]'' <small>(Emery, 1888)</small>
    *''[[Acromyrmex lundii]]'' <small>(Guérin-Méneville, 1838)</small>
    *''[[Acromyrmex niger]]'' <small>(Smith, 1858)</small>
    *''[[Acromyrmex nigrosetosus]]'' <small>(Forel, 1908)</small>
    *''[[Acromyrmex nobilis]]'' <small>Santschi, 1939</small>
    *''[[Acromyrmex octospinosus]]'' <small>(Reich, 1793)</small>
    *''[[Acromyrmex pubescens]]'' <small>(Emery, 1905)</small>
    *''[[Acromyrmex pulvereus]]'' <small>Santschi, 1919</small>
    *''[[Acromyrmex rugosus]]'' <small>(Smith, 1858)</small>
    *''[[Acromyrmex silvestrii]]'' <small>(Emery, 1905)</small>
    *''[[Acromyrmex striatus]]'' <small>(Roger, 1863)</small>
    *''[[Acromyrmex subterraneus]]'' <small>(Forel, 1893)</small>
    *''[[Acromyrmex versicolor]]'' <small>(Pergande, 1893)</small>
    *''[[Acromyrmex volcanus]]'' <small>Wheeler, 1937</small>
    {{div col end}}

    Acromyrmex: 32 taxa
    
### Links
- [AntWeb](http://www.antweb.org/)
- [AntCat](http://www.antcat.org/)
- [AntWiki](http://www.antwiki.org/)
- [Wikipedia's ant task force](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Insects/ant_task_force)
