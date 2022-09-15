var admin = db.getSiblingDB('admin');
admin.auth('root', 'password');
db = db.getSiblingDB('sudamerica_libre');
db.createCollection('bolivia');
db.bolivia.insertMany([
  {
  "message":"La Paz"
  },
  {
  "message":"Tarija"
  },
  {
   "message":"Oruro"
  },
  {
   "message":"Pando"
  },

]);