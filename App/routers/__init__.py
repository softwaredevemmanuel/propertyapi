from fastapi import APIRouter

#.......................................Authentication..................................
from Auth.routers.check_email import check_email_router
from Auth.routers.register import register_router
from Auth.routers.resend_verification_code import resend_email_verification_router
from Auth.routers.verify_code import verify_code_router
from Auth.routers.login import login_router
from Auth.routers.password_reset.request_pwd_reset import request_password_reset_router
from Auth.routers.password_reset.verify_code import verify_password_reset_code_router
from Auth.routers.password_reset.reset_pwd import reset_password_router

#.......................................Property..................................
# from Property.routers.listing_type import listing_type_router
# from Property.routers.property import property_router
# from Property.routers.opportunity import opportunity_router
# from Property.routers.investment_plan import investment_plan_router
# from Property.routers.subscription import subscription_router




router = APIRouter()

#.......................................Authentication..................................
router.include_router(router=check_email_router,tags=["Check Email Existence"])
router.include_router(router=register_router,tags=["Register A User"]) 
router.include_router(router=resend_email_verification_router,tags=["Resend Verification Code"]) 
router.include_router(router=verify_code_router,tags=["Verify Email With Code"])
router.include_router(router=login_router,tags=["Login A User"])
router.include_router(router=request_password_reset_router,tags=["Request a password reset"])
router.include_router(router=verify_password_reset_code_router,tags=["Verify Password reset code"])
router.include_router(router=reset_password_router,tags=["Reset User Password"])


#.......................................Property..................................
# router.include_router(router=listing_type_router,tags=["ListingType"])
# router.include_router(router=property_router,tags=["Property"])
# router.include_router(router=opportunity_router,tags=["OpportunityModel"])
# router.include_router(router=investment_plan_router,tags=["InvestmentPlan"])
# router.include_router(router=subscription_router,tags=["Subscription"])




