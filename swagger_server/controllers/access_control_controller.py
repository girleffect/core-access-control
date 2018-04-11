import connexion
import six
import connexion

from ge_core_shared import db_actions, decorators

from swagger_server.models.all_user_roles import AllUserRoles  # noqa: E501
from swagger_server.models.domain import Domain  # noqa: E501
from swagger_server.models.domain_role import DomainRole  # noqa: E501
from swagger_server.models.domain_role_update import DomainRoleUpdate  # noqa: E501
from swagger_server.models.domain_update import DomainUpdate  # noqa: E501
from swagger_server.models.invitation import Invitation  # noqa: E501
from swagger_server.models.invitation_domain_role import InvitationDomainRole  # noqa: E501
from swagger_server.models.invitation_site_role import InvitationSiteRole  # noqa: E501
from swagger_server.models.invitation_update import InvitationUpdate  # noqa: E501
from swagger_server.models.permission import Permission  # noqa: E501
from swagger_server.models.permission_update import PermissionUpdate  # noqa: E501
from swagger_server.models.resource import Resource  # noqa: E501
from swagger_server.models.resource_update import ResourceUpdate  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.role_resource_permission import RoleResourcePermission  # noqa: E501
from swagger_server.models.role_update import RoleUpdate  # noqa: E501
from swagger_server.models.site import Site  # noqa: E501
from swagger_server.models.site_role import SiteRole  # noqa: E501
from swagger_server.models.site_role_update import SiteRoleUpdate  # noqa: E501
from swagger_server.models.site_update import SiteUpdate  # noqa: E501
from swagger_server.models.user_domain_role import UserDomainRole  # noqa: E501
from swagger_server.models.user_site_role import UserSiteRole  # noqa: E501
from swagger_server import util


def access_control_roleresourcepermission_delete(role_id, resource_id, permission_id):  # noqa: E501
    """access_control_roleresourcepermission_delete

     # noqa: E501

    :param role_id: A unique integer value identifying the role.
    :type role_id: int
    :param resource_id: A unique integer value identifying the resource.
    :type resource_id: int
    :param permission_id: A unique integer value identifying the permission.
    :type permission_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="RoleResourcePermission",
        api_model=RoleResourcePermission,
        action="delete",
        query={
            "role_id": role_id,
            "resource_id": resource_id,
            "permission_id": permission_id
        }
    )


def domain_create(data=None):  # noqa: E501
    """domain_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: Domain
    """
    if connexion.request.is_json:
        data =connexion.request.get_json()

    return db_actions.crud(
        model="Domain",
        api_model=Domain,
        action="create",
        data=data,
    )


def domain_delete(domain_id):  # noqa: E501
    """domain_delete

     # noqa: E501

    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="Domain",
        api_model=Domain,
        action="delete",
        query={"id": domain_id},
    )


@decorators.list_response
def domain_list(offset=None, limit=None, parent_id=None, domain_ids=None):  # noqa: E501
    """domain_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param parent_id: An Optional query parameter to get all domains with the given parent_id.
    :type parent_id: int
    :param domain_ids: An optional list of domain ids
    :type domain_ids: List[int]

    :rtype: List[Domain]
    """
    return db_actions.crud(
        model="Domain",
        api_model=Domain,
        action="list",
        query={
            "offset": offset,
            "limit": limit,
            "ids": {
                "id": domain_ids,
                "parent_id": parent_id
            },
            "order_by": ["id"]
        }
    )


def domain_read(domain_id):  # noqa: E501
    """domain_read

     # noqa: E501

    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int

    :rtype: Domain
    """
    return db_actions.crud(
        model="Domain",
        api_model=Domain,
        action="read",
        query={"id": domain_id}
    )


def domain_update(domain_id, data=None):  # noqa: E501
    """domain_update

     # noqa: E501

    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int
    :param data:
    :type data: dict | bytes

    :rtype: Domain
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="Domain",
        api_model=Domain,
        action="update",
        data=data,
        query={"id": domain_id},
    )


def domainrole_create(data=None):  # noqa: E501
    """domainrole_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: DomainRole
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="DomainRole",
        api_model=DomainRole,
        action="create",
        data=data,
    )


def domainrole_delete(domain_id, role_id):  # noqa: E501
    """domainrole_delete

     # noqa: E501

    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="DomainRole",
        api_model=DomainRole,
        action="delete",
        query={
            "domain_id": domain_id,
            "role_id": role_id,
        }
    )


@decorators.list_response
def domainrole_list(offset=None, limit=None, domain_id=None, role_id=None):  # noqa: E501
    """domainrole_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param domain_id: An optional query parameter to filter by domain_id
    :type domain_id: int
    :param role_id: An optional query parameter to filter by role_id
    :type role_id: int

    :rtype: List[DomainRole]
    """
    return db_actions.crud(
        model="DomainRole",
        api_model=DomainRole,
        action="list",
        query={
            "offset": offset,
            "limit": limit,
            "ids": {"domain_id": domain_id, "role_id": role_id},
            "order_by": ["domain_id"]}
    )


def domainrole_read(domain_id, role_id):  # noqa: E501
    """domainrole_read

     # noqa: E501

    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: DomainRole
    """
    return db_actions.crud(
        model="DomainRole",
        api_model=DomainRole,
        action="read",
        query={
            "domain_id": domain_id,
            "role_id": role_id,
        }
    )


def domainrole_update(domain_id, role_id, data=None):  # noqa: E501
    """domainrole_update

     # noqa: E501

    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int
    :param data:
    :type data: dict | bytes

    :rtype: DomainRole
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="DomainRole",
        api_model=DomainRole,
        action="update",
        data=data,
        query={
            "domain_id": domain_id,
            "role_id": role_id,
        },
    )


def invitation_create(data=None):  # noqa: E501
    """invitation_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: Invitation
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    # return db_actions.crud(
    #     model="Invitation",
    #     api_model=Invitation,
    #     action="create",
    #     data=data,
    # )
    raise NotImplementedError()

def invitation_delete(invitation_id):  # noqa: E501
    """invitation_delete

     # noqa: E501

    :param invitation_id: A UUID value identifying the invitation.
    :type invitation_id: dict | bytes

    :rtype: None
    """
    # return db_actions.crud(
    #     model="Invitation",
    #     api_model=Invitation,
    #     action="delete",
    #     query={
    #         "invitation_id": invitation_id,
    #     }
    # )
    raise NotImplementedError()

@decorators.list_response
def invitation_list(offset=None, limit=None, invitor_id=None, invitation_ids=None):  # noqa: E501
    """invitation_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param invitor_id: Optional filter based on the invitor (the user who created the invitation)
    :type invitor_id: dict | bytes
    :param invitation_ids: An optional list of invitation ids
    :type invitation_ids: List[str]

    :rtype: List[Invitation]
    """
    # return db_actions.crud(
    #     model="Invitation",
    #     api_model=Invitation,
    #     action="list",
    #     query={
    #         "offset": offset,
    #         "limit": limit,
    #         "ids": {
    #             "invitor_id": invitor_id,
    #             "invitation_ids": invitation_ids
    #         },
    #         "order_by": ["invitor_id"]}
    # )
    raise NotImplementedError()

def invitation_read(invitation_id):  # noqa: E501
    """invitation_read

     # noqa: E501

    :param invitation_id: A UUID value identifying the invitation.
    :type invitation_id: dict | bytes

    :rtype: Invitation
    """
    # return db_actions.crud(
    #     model="Invitation",
    #     api_model=Invitation,
    #     action="read",
    #     query={
    #         "invitation_id": invitation_id
    #     }
    # )
    raise NotImplementedError()

def invitation_redeem(invitation_id, user_id):  # noqa: E501
    """invitation_redeem

    Assign all roles assigned to the invitation to the specified user, removing the invitation and related configuration when done. Note: We may have to change the role assignment to an asynchronous task depending on the complexity of the implementation. # noqa: E501

    :param invitation_id: A UUID value identifying the invitation.
    :type invitation_id: dict | bytes
    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes

    :rtype: AllUserRoles
    """
    raise NotImplementedError()


def invitation_update(invitation_id, data=None):  # noqa: E501
    """invitation_update

     # noqa: E501

    :param invitation_id: A UUID value identifying the invitation.
    :type invitation_id: dict | bytes
    :param data:
    :type data: dict | bytes

    :rtype: Invitation
    """
    raise NotImplementedError()



def invitationdomainrole_create(data=None):  # noqa: E501
    """invitationdomainrole_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: InvitationDomainRole
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    # return db_actions.crud(
    #     model="InvitationDomainRole",
    #     api_model=InvitationDomainRole,
    #     action="create",
    #     data=data,
    # )
    raise NotImplementedError()

def invitationdomainrole_delete(invitation_id, domain_id, role_id):  # noqa: E501
    """invitationdomainrole_delete

     # noqa: E501

    :param invitation_id: A UUID value identifying the invitation.
    :type invitation_id: dict | bytes
    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: None
    """
    # return db_actions.crud(
    #     model="InvitaionDomainRole",
    #     api_model=InvitationDomainRole,
    #     action="delete",
    #     query={
    #         "invitaion_id": invitation_id,
    #         "domain_id": domain_id,
    #         "role_id": role_id,
    #     }
    # )
    raise NotImplementedError()

@decorators.list_response
def invitationdomainrole_list(offset=None, limit=None, invitation_id=None, domain_id=None, role_id=None):  # noqa: E501
    """invitationdomainrole_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param invitation_id: An optional query parameter to filter by invitation_id
    :type invitation_id: dict | bytes
    :param domain_id: An optional query parameter to filter by domain_id
    :type domain_id: int
    :param role_id: An optional query parameter to filter by role_id
    :type role_id: int

    :rtype: List[InvitationDomainRole]
    """
    # return db_actions.crud(
    #     model="InvitationDomainRole",
    #     api_model=InvitationDomainRole,
    #     action="list",
    #     query={
    #         "offset": offset,
    #         "limit": limit,
    #         "ids": {
    #             "invitation_id": invitation_id,
    #             "domain_id": domain_id,
    #             "role_id": role_id
    #         },
    #         "order_by": ["domain_id"]}
    # )
    raise NotImplementedError()


def invitationdomainrole_read(invitation_id, domain_id, role_id):  # noqa: E501
    """invitationdomainrole_read

     # noqa: E501

    :param invitation_id: A UUID value identifying the invitation.
    :type invitation_id: dict | bytes
    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: InvitationDomainRole
    """
    # return db_actions.crud(
    #     model="InvitationDomainRole",
    #     api_model=InvitationDomainRole,
    #     action="read",
    #     query={
    #         "invitation_id": invitation_id,
    #         "domain_id": domain_id,
    #         "role_id": role_id,
    #     }
    # )
    raise NotImplementedError()

def invitationsiterole_create(data=None):  # noqa: E501
    """invitationsiterole_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: InvitationSiteRole
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    # return db_actions.crud(
    #     model="InvitationSiteRole",
    #     api_model=InvitationSiteRole,
    #     action="create",
    #     data=data,
    # )
    raise NotImplementedError()


def invitationsiterole_delete(invitation_id, site_id, role_id):  # noqa: E501
    """invitationsiterole_delete

     # noqa: E501

    :param invitation_id: A UUID value identifying the invitation.
    :type invitation_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: None
    """
    # return db_actions.crud(
    #     model="InvitationSiteRole",
    #     api_model=InvitationSiteRole,
    #     action="delete",
    #     query={
    #         "invitaion_id": invitation_id,
    #         "site_id": site_id,
    #         "role_id": role_id,
    #     }
    # )
    raise NotImplementedError()

@decorators.list_response
def invitationsiterole_list(offset=None, limit=None, invitation_id=None, site_id=None, role_id=None):  # noqa: E501
    """invitationsiterole_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param invitation_id: An optional query parameter to filter by invitation_id
    :type invitation_id: dict | bytes
    :param site_id: An optional query parameter to filter by site_id
    :type site_id: int
    :param role_id: An optional query parameter to filter by role_id
    :type role_id: int

    :rtype: List[InvitationSiteRole]
    # """
    # return db_actions.crud(
    #     model="InvitationSiteRole",
    #     api_model=InvitationSiteRole,
    #     action="list",
    #     query={
    #         "offset": offset,
    #         "limit": limit,
    #         "ids": {
    #             "invitation_id": invitation_id,
    #             "site_id": site_id,
    #             "role_id": role_id
    #         },
    #         "order_by": ["site_id"]}
    # )
    raise NotImplementedError()


def invitationsiterole_read(invitation_id, site_id, role_id):  # noqa: E501
    """invitationsiterole_read

     # noqa: E501

    :param invitation_id: A UUID value identifying the invitation.
    :type invitation_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: InvitationSiteRole
    """
    # return db_actions.crud(
    #     model="InvitationSiteRole",
    #     api_model=InvitationSiteRole,
    #     action="read",
    #     query={
    #         "invitation_id": invitation_id,
    #         "site_id": site_id,
    #         "role_id": role_id,
    #     }
    # )
    raise NotImplementedError()

def permission_create(data=None):  # noqa: E501
    """permission_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: Permission
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="Permission",
        api_model=Permission,
        action="create",
        data=data,
    )


def permission_delete(permission_id):  # noqa: E501
    """permission_delete

     # noqa: E501

    :param permission_id: A unique integer value identifying the permission.
    :type permission_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="Permission",
        api_model=Permission,
        action="delete",
        query={"id": permission_id},
    )


@decorators.list_response
def permission_list(offset=None, limit=None, permission_ids=None):  # noqa: E501
    """permission_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param permission_ids: An optional list of permission ids
    :type permission_ids: List[int]

    :rtype: List[Permission]
    """
    return db_actions.crud(
        model="Permission",
        api_model=Permission,
        action="list",
        query={"offset": offset, "limit": limit, "ids": permission_ids, "order_by": ["id"]}
    )


def permission_read(permission_id):  # noqa: E501
    """permission_read

     # noqa: E501

    :param permission_id: A unique integer value identifying the permission.
    :type permission_id: int

    :rtype: Permission
    """
    return db_actions.crud(
        model="Permission",
        api_model=Permission,
        action="read",
        query={"id": permission_id}
    )


def permission_update(permission_id, data=None):  # noqa: E501
    """permission_update

     # noqa: E501

    :param permission_id: A unique integer value identifying the permission.
    :type permission_id: int
    :param data:
    :type data: dict | bytes

    :rtype: Permission
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="Permission",
        api_model=Permission,
        action="update",
        data=data,
        query={"id": permission_id},
    )


def resource_create(data=None):  # noqa: E501
    """resource_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: Resource
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="Resource",
        api_model=Resource,
        action="create",
        data=data,
    )


def resource_delete(resource_id):  # noqa: E501
    """resource_delete

     # noqa: E501

    :param resource_id: A unique integer value identifying the resource.
    :type resource_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="Resource",
        api_model=Resource,
        action="delete",
        query={"id": resource_id},
    )


@decorators.list_response
def resource_list(offset=None, limit=None, prefix=None, resource_ids=None):  # noqa: E501
    """resource_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param prefix: An optional URN prefix filter
    :type prefix: str
    :param resource_ids: An optional list of resource ids
    :type resource_ids: List[int]

    :rtype: List[Resource]
    """
    return db_actions.crud(
        model="Resource",
        api_model=Resource,
        action="list",
        query={"offset": offset, "limit": limit, "ids": resource_ids, "order_by": ["id"]}
    )


def resource_read(resource_id):  # noqa: E501
    """resource_read

     # noqa: E501

    :param resource_id: A unique integer value identifying the resource.
    :type resource_id: int

    :rtype: Resource
    """
    return db_actions.crud(
        model="Resource",
        api_model=Resource,
        action="read",
        query={"id": resource_id}
    )


def resource_update(resource_id, data=None):  # noqa: E501
    """resource_update

     # noqa: E501

    :param resource_id: A unique integer value identifying the resource.
    :type resource_id: int
    :param data:
    :type data: dict | bytes

    :rtype: Resource
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="Resource",
        api_model=Resource,
        action="update",
        data=data,
        query={"id": resource_id},
    )


def role_create(data=None):  # noqa: E501
    """role_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: Role
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="Role",
        api_model=Role,
        action="create",
        data=data,
    )


def role_delete(role_id):  # noqa: E501
    """role_delete

     # noqa: E501

    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="Role",
        api_model=Role,
        action="delete",
        query={"id": role_id},
    )


@decorators.list_response
def role_list(offset=None, limit=None, role_ids=None):  # noqa: E501
    """role_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param role_ids: An optional list of role ids
    :type role_ids: List[int]

    :rtype: List[Role]
    """
    return db_actions.crud(
        model="Role",
        api_model=Role,
        action="list",
        query={"offset": offset, "limit": limit, "ids": role_ids, "order_by": ["id"]}
    )


def role_read(role_id):  # noqa: E501
    """role_read

     # noqa: E501

    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: Role
    """
    return db_actions.crud(
        model="Role",
        api_model=Role,
        action="read",
        query={"id": role_id}
    )


def role_update(role_id, data=None):  # noqa: E501
    """role_update

     # noqa: E501

    :param role_id: A unique integer value identifying the role.
    :type role_id: int
    :param data:
    :type data: dict | bytes

    :rtype: Role
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="Role",
        api_model=Role,
        action="update",
        data=data,
        query={"id": role_id},
    )


def roleresourcepermission_create(data=None):  # noqa: E501
    """roleresourcepermission_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: RoleResourcePermission
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="RoleResourcePermission",
        api_model=RoleResourcePermission,
        action="create",
        data=data,
    )


@decorators.list_response
def roleresourcepermission_list(offset=None, limit=None, role_id=None, resource_id=None, permission_id=None):  # noqa: E501
    """roleresourcepermission_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param role_id: An optional query parameter to filter by role_id
    :type role_id: int
    :param resource_id: An optional resource filter
    :type resource_id: int
    :param permission_id: An optional permission filter
    :type permission_id: int

    :rtype: List[RoleResourcePermission]
    """
    return db_actions.crud(
        model="RoleResourcePermission",
        api_model=RoleResourcePermission,
        action="list",
        query={
            "offset": offset,
            "limit": limit,
            "ids": {"role_id": role_id, "resource_id": resource_id, "permission_id": permission_id},
            "order_by": ["role_id"]}
    )


def roleresourcepermission_read(role_id, resource_id, permission_id):  # noqa: E501
    """roleresourcepermission_read

     # noqa: E501

    :param role_id: A unique integer value identifying the role.
    :type role_id: int
    :param resource_id: A unique integer value identifying the resource.
    :type resource_id: int
    :param permission_id: A unique integer value identifying the permission.
    :type permission_id: int

    :rtype: RoleResourcePermission
    """
    return db_actions.crud(
        model="RoleResourcePermission",
        api_model=RoleResourcePermission,
        action="read",
        query={
            "role_id": role_id,
            "resource_id": resource_id,
            "permission_id": permission_id
        }
    )


def site_create(data=None):  # noqa: E501
    """site_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: Site
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="Site",
        api_model=Site,
        action="create",
        data=data,
    )


def site_delete(site_id):  # noqa: E501
    """site_delete

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="Site",
        api_model=Site,
        action="delete",
        query={"id": site_id},
    )


@decorators.list_response
def site_list(offset=None, limit=None, site_ids=None):  # noqa: E501
    """site_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param site_ids: An optional list of site ids
    :type site_ids: List[int]

    :rtype: List[Site]
    """
    return db_actions.crud(
        model="Site",
        api_model=Site,
        action="list",
        query={"offset": offset, "limit": limit, "ids": site_ids, "order_by": ["id"]}
    )


def site_read(site_id):  # noqa: E501
    """site_read

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: Site
    """
    return db_actions.crud(
        model="Site",
        api_model=Site,
        action="read",
        query={"id": site_id}
    )


def site_update(site_id, data=None):  # noqa: E501
    """site_update

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param data:
    :type data: dict | bytes

    :rtype: Site
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="Site",
        api_model=Site,
        action="update",
        data=data,
        query={"id": site_id},
    )


def siterole_create(data=None):  # noqa: E501
    """siterole_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: SiteRole
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="SiteRole",
        api_model=SiteRole,
        action="create",
        data=data,
    )


def siterole_delete(site_id, role_id):  # noqa: E501
    """siterole_delete

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="SiteRole",
        api_model=SiteRole,
        action="delete",
        query={
            "site_id": site_id,
            "role_id": role_id,
        }
    )


@decorators.list_response
def siterole_list(offset=None, limit=None, site_id=None, role_id=None):  # noqa: E501
    """siterole_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param site_id: An optional query parameter to filter by site_id
    :type site_id: int
    :param role_id: An optional query parameter to filter by role_id
    :type role_id: int

    :rtype: List[SiteRole]
    """
    return db_actions.crud(
        model="SiteRole",
        api_model=SiteRole,
        action="list",
        query={
            "offset": offset,
            "limit": limit,
            "ids": {"site_id": site_id, "role_id": role_id},
            "order_by": ["site_id"]}
    )


def siterole_read(site_id, role_id):  # noqa: E501
    """siterole_read

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: SiteRole
    """
    return db_actions.crud(
        model="SiteRole",
        api_model=SiteRole,
        action="read",
        query={
            "site_id": site_id,
            "role_id": role_id,
        }
    )


def siterole_update(site_id, role_id, data=None):  # noqa: E501
    """siterole_update

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int
    :param data:
    :type data: dict | bytes

    :rtype: SiteRole
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="SiteRole",
        api_model=SiteRole,
        action="update",
        data=data,
        query={
            "site_id": site_id,
            "role_id": role_id,
        },
    )


def userdomainrole_create(data=None):  # noqa: E501
    """userdomainrole_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: UserDomainRole
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="UserDomainRole",
        api_model=UserDomainRole,
        action="create",
        data=data,
    )

def userdomainrole_delete(user_id, domain_id, role_id):  # noqa: E501
    """userdomainrole_delete

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: None
    """
    return db_actions.crud(
        model="UserDomainRole",
        api_model=UserDomainRole,
        action="delete",
        query={
            "user_id": user_id,
            "domain_id": domain_id,
            "role_id": role_id,
        }
    )

@decorators.list_response
def userdomainrole_list(offset=None, limit=None, user_id=None, domain_id=None, role_id=None):  # noqa: E501
    """userdomainrole_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param user_id: An optional query parameter to filter by user_id
    :type user_id: dict | bytes
    :param domain_id: An optional query parameter to filter by domain_id
    :type domain_id: int
    :param role_id: An optional query parameter to filter by role_id
    :type role_id: int

    :rtype: List[UserDomainRole]
    """
    return db_actions.crud(
        model="UserDomainRole",
        api_model=UserDomainRole,
        action="list",
        query={
            "offset": offset,
            "limit": limit,
            "ids": {
                "user_id": user_id,
                "domain_id": domain_id,
                "role_id": role_id
            },
            "order_by": ["user_id"]}
    )

def userdomainrole_read(user_id, domain_id, role_id):  # noqa: E501
    """userdomainrole_read

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param domain_id: A unique integer value identifying the domain.
    :type domain_id: int
    :param role_id: A unique integer value identifying the role.
    :type role_id: int

    :rtype: UserDomainRole
    """
    return db_actions.crud(
        model="UserDomainRole",
        api_model=UserDomainRole,
        action="read",
        query={
            "user_id": user_id,
            "domain_id": domain_id,
            "role_id": role_id,
        }
    )

def usersiterole_create(data=None):  # noqa: E501
    """usersiterole_create

     # noqa: E501

    :param data:
    :type data: dict | bytes

    :rtype: UserSiteRole
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()

    return db_actions.crud(
        model="UserSiteRole",
        api_model=UserSiteRole,
        action="create",
        data=data,
    )


@decorators.list_response
def usersiterole_list(offset=None, limit=None, user_id=None, site_id=None, role_id=None):  # noqa: E501
    """usersiterole_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param user_id: An optional query parameter to filter by user_id
    :type user_id: dict | bytes
    :param site_id: An optional query parameter to filter by site_id
    :type site_id: int
    :param role_id: An optional query parameter to filter by role_id
    :type role_id: int

    :rtype: List[UserSiteRole]
    """
    return db_actions.crud(
        model="UserSiteRole",
        api_model=UserSiteRole,
        action="list",
        query={
            "offset": offset,
            "limit": limit,
            "ids": {
                "user_id": user_id,
                "site_id": site_id,
                "role_id": role_id
            },
            "order_by": ["site_id"]}
    )


def usersiterole_read(user_id, site_id, role_id):
    return db_actions.crud(
        model="UserSiteRole",
        api_model=UserSiteRole,
        action="read",
        query={
            "user_id": user_id,
            "site_id": site_id,
            "role_id": role_id,
        }
    )


def usersiterole_delete(user_id, site_id, role_id):
    return db_actions.crud(
        model="UserSiteRole",
        api_model=UserSiteRole,
        action="delete",
        query={
            "user_id": user_id,
            "site_id": site_id,
            "role_id": role_id,
        }
    )
