from resources.auth_resource import (
    RegisterUser,
    LoginUser,
    RegisterSeller,
    LoginSeller,
    LoginAdmin,
    Login,
    Logout,
)
from resources.home_resource import HomeResource, GetHomeResource, HomesResource, HomeDetailsResource
from resources.visitation_resource import VisitationResource
from resources.land_resource import LandResource, LandsResource, LandDetalisResource
from resources.meeting_resource import MeetingResource
from resources.message_resource import MessageResource, ChatHistoryResource, ChatInterlocutorsResource

routes = (
    (Logout, "/logout"),
    (RegisterUser, "/user/register-user"),
    (LoginUser, "/user/login-user"),
    (RegisterSeller, "/user/register-seller"),
    (LoginSeller, "/user/login-seller"),
    (Login, "/user/login"),
    (LoginAdmin, "/user/login-admin"),
    (HomeResource, "/home"),
    (HomesResource, "/homes"),
    (GetHomeResource, "/home/<int:home_id>"),
    (HomeDetailsResource, "/home-details/<int:home_id>"),
    (VisitationResource, "/visitation"),
    (LandResource, "/land"),
    (LandDetalisResource, "/land-details/<int:land_id>"),
    (LandsResource, "/lands"),
    (MeetingResource, "/meeting"),
    (MessageResource, "/message"),
    (ChatHistoryResource, "/message/<int:interlocutor_id>"),
    (ChatInterlocutorsResource, "/message/interlocutors"),
)