"""
This script will sync photos from a flickr account (by tag or set) to a directory on the computer.

If you set your desktop background to use photos from this folder, then it will update as you update your albums/photostream

Future plans:
- Pull from multiple sources
- Push photos to the queues of friends.


Dependencies:
https://github.com/alexis-mignon/python-flickr-api.git

"""
# Other libraries / includes
import flickr_api as f
import os

# ================================================ # 
# Variables

flickr_user = 'cmccarty87'
photoset_id = '72157632820330654' # kauai
user_id = '55204569@N00'


# ================================================ # 
# Functions

def auth():
	f.set_auth_handler(access_token)


def getPhotosInSet(photoset_id):
	u = f.Person.findByUserName(flickr_user)
	ps = u.getPhotosets()
	
	for p in ps:
		if p.id == photoset_id:
			return p.getPhotos()
			
	return None
	
def getPhotosInTag(tag):
	#w = Walker(Photo.search,tags = tag)
 	#print 
	
	
	#d = {'tags': tag}
	photos = f.Photo.search(tags=tag, user_id=user_id)
	return photos

		
	"""
		"tags" => $tags,
		"per_page" => $limit,
		"extras" => "geo",
		"sort" => "date-taken-asc",
	"""	
	
def clear_cache():
	print 'Clearing the cache...'
	cmd = 'rm cache/*.jpg'
	os.system(cmd)
		
# ================================================ # 

def main():
	print 'Run...'
	tag = 'gw:peru'
	tag = 'greece2012'

	# clear out the existing photos
	clear_cache()


	photos = getPhotosInTag(tag)
	#photos = getPhotosInSet(photoset_id)
	
	for photo in photos:
		print photo.title, photo.id
	
		photo.save('cache/%s.jpg' % photo.title)
	
	
	
if __name__ == '__main__':
	main()