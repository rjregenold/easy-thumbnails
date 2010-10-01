# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Source'
        db.create_table('easy_thumbnails_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storage_hash', self.gf('django.db.models.fields.CharField')(max_length=40, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 10, 1, 0, 9, 47, 385857))),
        ))
        db.send_create_signal('easy_thumbnails', ['Source'])

        # Adding model 'Thumbnail'
        db.create_table('easy_thumbnails_thumbnail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storage_hash', self.gf('django.db.models.fields.CharField')(max_length=40, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 10, 1, 0, 9, 47, 385857))),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='thumbnails', to=orm['easy_thumbnails.Source'])),
        ))
        db.send_create_signal('easy_thumbnails', ['Thumbnail'])


    def backwards(self, orm):
        
        # Deleting model 'Source'
        db.delete_table('easy_thumbnails_source')

        # Deleting model 'Thumbnail'
        db.delete_table('easy_thumbnails_thumbnail')


    models = {
        'easy_thumbnails.source': {
            'Meta': {'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 10, 1, 0, 9, 47, 385857)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'storage_hash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'})
        },
        'easy_thumbnails.thumbnail': {
            'Meta': {'object_name': 'Thumbnail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 10, 1, 0, 9, 47, 385857)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thumbnails'", 'to': "orm['easy_thumbnails.Source']"}),
            'storage_hash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'})
        }
    }

    complete_apps = ['easy_thumbnails']
