# Geoname annotator
from epitator.annotator import AnnoDoc
from epitator.geoname_annotator import GeonameAnnotator

doc = AnnoDoc("Where is Chiang Mai?")
doc.add_tiers(GeonameAnnotator())

annotations = doc.tiers["geonames"].spans
geoname = annotations[0].geoname
geoname['name']
# = 'Chiang Mai'
geoname['geonameid']
# = '1153671'
geoname['latitude']
# = 18.79038
geoname['longitude']
# = 98.98468

from epitator.spacy_annotator import SpacyAnnotator
spacy_token_tier = doc.require_tiers('spacy.tokens', via=SpacyAnnotator)
list(geoname_annotier.group_spans_by_containing_span(spacy_token_tier))


# Disease entities

from epitator.annotator import AnnoDoc
from epitator.resolved_keyword_annotator import ResolvedKeywordAnnotator
from tika import parser
 
raw = parser.from_file('H1N1.pdf')
    
doc = AnnoDoc(raw['content'])

doc.add_tiers(ResolvedKeywordAnnotator())

annotations = doc.tiers["resolved_keywords"].spans

for k in annotations:
    print(k.metadata["resolutions"])


# Counts cases

from epitator.annotator import AnnoDoc
from epitator.count_annotator import CountAnnotator

from tika import parser
 
raw = parser.from_file('H1N1.pdf')

doc = AnnoDoc(raw['content'])
doc.add_tiers(CountAnnotator())
annotations = doc.tiers["counts"].spans

for i in annotations:
    
    print(i.metadata)




# Date annotator

from epitator.annotator import AnnoDoc
from epitator.date_annotator import DateAnnotator
from tika import parser
 
raw = parser.from_file('H1N1.pdf')

doc = AnnoDoc(raw['content'])

doc.add_tiers(DateAnnotator())
annotations = doc.tiers["dates"].spans

for i in annotations:
    
    print(i.metadata["datetime_range"])
# = [datetime.datetime(1988, 3, 5, 0, 0), datetime.datetime(1988, 4, 7, 0, 0)]


# Structured data annotator

from epitator.annotator import AnnoDoc
from epitator.structured_data_annotator import StructuredDataAnnotator
from tika import parser
 
raw = parser.from_file('H1N1.pdf')

doc = AnnoDoc(raw['content'])


doc.add_tiers(StructuredDataAnnotator())
annotations = doc.tiers["structured_data"].spans
annotations[10].metadata



#Incident annotator

from epitator.annotator import AnnoDoc
from epitator.structured_incident_annotator import StructuredIncidentAnnotator
doc = AnnoDoc("""
Fictional October 2015 rabies cases in Svalbard

species | cases | deaths
Cattle  | 0     | 0
Dogs    | 4     | 1
""")
doc.add_tiers(StructuredIncidentAnnotator())
annotations = doc.tiers["structured_incidents"].spans
annotations[-1].metadata
