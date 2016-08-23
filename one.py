from flask import Flask, request,jsonify
import logging,random,threading,time
import os
import re
import pickle,json
import pymongo
from d9t.json import parser
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
MONGO_URI = 'mongodb://amnox:aMNOX123BITCH@ds153835.mlab.com:53835/heroku_w6n26w98'
client=(pymongo.MongoClient(MONGO_URI))
mc=client.get_default_database()
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
class HelloWorld(Resource):

    def get(self):
        return "post array of likes object with fields [{'name':<>,'category':<>,'about':<>,'description':<>,'genre':<>}] \n limit array size to 10!!"
    def post(self):
        
        stuff=[]
        class counter(object):
            def __init__(self):
                
                self.lock=threading.Lock()
                self.amnoxDB=mc
                self.the_json_list=[]
                self.count_json_var=0
            def make_json(self,list):
                self.the_json_list.append({'name':list[0],'sub-category':list[1],'category':list[2]})
        
        
            def first(self,keyword):
                cc=self.amnoxDB.book_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                for shit in cc:
            
                    try:
                        if keyword[0] in str(shit['name'][0].encode('ascii', 'ignore')).lower():
                            self.make_json([shit['name'],[shit['genre'][0].encode('ascii', 'ignore')],['Books']])
                    except KeyError:
                        continue
        
                self.lock.release()
            def second(self,keyword):
        
                cc=self.amnoxDB.college_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                for shit in cc:
            
                    try:
                        if str(shit['name'][0]).lower()==keyword[0]:
                            self.make_json([str(shit['name']),[str(shit['category'])],['Universities']])
                    except KeyError:
                        continue
        
                self.lock.release()
            def third(self,keyword):
        
                cc=self.amnoxDB.cricket_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                for shit in cc:
            
                    try:
                        if str(shit['name'][0]).lower()==keyword[0]:
                            self.make_json([(shit['name']),['Team '+(shit['team'][0]),str(shit['role'][0])],['Cricket']])
                    except KeyError:
                        continue
        
                self.lock.release()
            def fourth(self,keyword):
        
                cc=self.amnoxDB.football_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                for shit in cc:
            
                    try:
                        if str(shit['name'][0]).lower()==keyword[0]:
                            self.make_json([(shit['name']),(shit['club']),['Football']])
                    except KeyError:
                        continue
        
                self.lock.release()
            def fifth(self,keyword):
        
                cc=self.amnoxDB.movies_eng_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                for shit in cc:
            
                    try:
                        if keyword[0] in str(shit['name'][0].encode('ascii', 'ignore')).lower():
                            self.make_json([[shit['name'][0].encode('ascii', 'ignore')],shit['genre'],['Movies']])
                    except KeyError,UnicodeEncodeError:
                        continue
        
                self.lock.release()
            def sixth(self,keyword):
        
                cc=self.amnoxDB.movies_hin_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                for shit in cc:
            
                    try:
                        if keyword[0] in str(shit['name'][0].encode('ascii', 'ignore')).lower():
                            self.make_json([[shit['name'][0].encode('ascii', 'ignore')],shit['genre'],['Movies']])
                    except KeyError,UnicodeEncodeError:
                        continue
                self.lock.release()
            def seventh(self,keyword):
        
                cc=self.amnoxDB.top_pages_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                for shit in cc:
            
                    try:
                        if str(shit['name'][0].encode('ascii', 'ignore')).lower() in keyword[0]:
                            self.make_json([shit['name'],shit['category'],['Shows']])
                    except KeyError,UnicodeEncodeError:
                        continue
                self.lock.release()
            def eighth(self,keyword):
        
                cc=self.amnoxDB.tv_series_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                cd=self.amnoxDB.top_pages_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                for shit in cc:
            
                    try:
                        if keyword[0] in str(shit['name'][0].encode('ascii', 'ignore')).lower():
                            self.make_json([shit['name'],shit['genre'],['Shows']])
                    except KeyError,UnicodeEncodeError:
                        continue
        
                for shit in cd:
                    try:
                        for shits in shit['category']:
                            if 'show' in shits.lower():
                                if keyword[0] in str(shit['name'][0].encode('ascii', 'ignore')).lower():
                                    self.make_json([shit['name'],shit['category'],['Shows']])
                        
                    except KeyError:
                        continue
                self.lock.release()
            def ninth(self,keyword):
        
                cc=self.amnoxDB.top_pages_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                cf=self.amnoxDB.book_dict.find({'author': re.compile(keyword, re.IGNORECASE)})
                cg=self.amnoxDB.movies_eng_dict.find({'actors': re.compile(keyword, re.IGNORECASE)})
                ch=self.amnoxDB.movies_hin_dict.find({'actors': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                if 'public figure' in keyword[1]:
                    for shit in cc:
                
                        try:
                            if str(shit['name'][0].encode('ascii', 'ignore')).lower() in keyword[0]:
                                self.make_json([shit['name'][0].encode('ascii', 'ignore'),shit['category'],['People']])
                        except KeyError,UnicodeEncodeError:
                            continue
                if 'author' in keyword[1]:
                    category=[]
                    name=''
                    for shit in cf:
                
                        for shits in shit['author']:
                            if shits.lower() in keyword[0]:
                                name=str(shits)
                                category.extend(shit['genre'])
                                break
                    if name!='':
                        self.make_json([[name],list(set(category)),['Authors']])
                if 'actor' in keyword[1]:
                    category=[]
                    name=''
                    for shit in cg:
                        try:
                            for shits in shit['actors']:
                                if shits.lower() in keyword[0]:
                                    name= str(shits)
                                    category.extend(shit['genre'])
                                    break
                        except KeyError:
                            continue
                    if len(set(category))>0:
                        self.make_json([[name],list(set(category)),['Actors']])
                    for shit in ch:
                        try:
                            for shits in shit['actors']:
                                if shits.lower() in keyword[0]:
                                    print shits
                        except KeyError:
                            continue
                if 'politic' in keyword[1]:
                    self.make_json([[keyword[0]],[keyword[1]],['People']])
                self.lock.release()
            def tenth(self,keyword):
                cc=self.amnoxDB.top_pages_dict.find({'name': re.compile(keyword, re.IGNORECASE)})
                self.lock.acquire()
                for shit in cc:
                    for shits in shit['name']:
                        if keyword[0] in shits.lower():
                            self.make_json([shits,shit['category'],['Media']])
                self.lock.release()
            def eleventh(self,keyword):
                self.lock.acquire()
                if keyword[2]!=None:
                    self.make_json([[keyword[0]],keyword[2],['Musician']])
                self.lock.release()
        this_guy=counter()
        def worker(keyword,current_item):
            
            lock=threading.Lock()
            people=['public figure','musician','actor','author','politician']
            pause=random.random()
            if 'book' in keyword[1]:
                this_guy.first(keyword)
                stuff.remove(current_item)
            if 'university' in keyword[1]:
                this_guy.second(keyword)
                stuff.remove(current_item)
            if 'athlete' in keyword[1]:
                this_guy.fourth(keyword)
                this_guy.third(keyword)
                stuff.remove(current_item)
            if 'movie' in keyword[1]:
                this_guy.fifth(keyword)
                this_guy.sixth(keyword)
                stuff.remove(current_item)
            if 'show' in keyword[1]:
                this_guy.eighth(keyword)
                this_guy.seventh(keyword)
                stuff.remove(current_item)
            for shit in ['public figure','author','actor','politic']:
                if shit in keyword[1]:
                    this_guy.ninth(keyword)
                    stuff.remove(current_item)
            for shit in ['publishing']:
                if shit in keyword[1]:
                    this_guy.tenth(keyword)
                    stuff.remove(current_item)
            if 'music' in keyword[1]:
                this_guy.eleventh(keyword)
                stuff.remove(current_item)
        stuff=request.get_json()

        threads=[]
        start = time.clock()
        print 'started/...'
        for shit in stuff:
            if (shit['genre'] is not None):
                shit_show=[(shits.rstrip()).lstrip() for shits in re.split(r'[`\=~!@#$%^*()_+\[\]{};\'\\:"|<,./<>?]', shit['genre']) if len(shits)>=3]
                t = threading.Thread(target=worker, args=(((shit['name']).lower(),(shit['category']).lower(),shit_show),shit))
            else:
                t = threading.Thread(target=worker, args=(((shit['name']).lower(),(shit['category']).lower(),None),shit))
            t.start()
            threads.append(t)
        for t in threads:
            print 'im on one'
            t.join()
        print time.clock() - start
        aa=json.dumps(this_guy.the_json_list, default=lambda o: o.__dict__)
        return json.loads(aa)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)