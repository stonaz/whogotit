from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        print 'owner: ' + str(type(obj.owner))
        print 'user:' + str(type(request.user))
        print obj.owner == request.user
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
    
    
class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            print view
            return True

        ## Write permissions are only allowed to the owner of the snippet.
        #print obj.owner
        #print request.user
        #cacca
        #if obj.owner == request.user:
        #    return True