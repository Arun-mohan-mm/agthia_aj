from django.urls import path
import agthi.views


urlpatterns = [
    path('',agthi.views.home,name='home'),
    path('home', agthi.views.home, name='home'),
    path('register_admin', agthi.views.register_admin, name='register_admin'),
    path('abt_us', agthi.views.abt_us, name='abt_us'),
    path('our_people', agthi.views.our_ple, name='our_people'),
    path('mission', agthi.views.miss_ion, name='mission'),
    path('vision', agthi.views.vis_ion, name='vision'),
    path('word_from_ceo', agthi.views.word_from_ceo, name='word_from_ceo'),
    path('careers', agthi.views.careers, name='careers'),
    path('restaurants', agthi.views.restaurants, name='restaurants'),
    path('reservation', agthi.views.reservation, name='reservation'),
    path('contact', agthi.views.contact, name='contact'),
    path('single_product/<id>', agthi.views.single_product, name='single_product'),
    path('book_table', agthi.views.book_table, name='book_table'),
    path('contact_cust', agthi.views.contact_cust, name='contact_cust'),
    path('login', agthi.views.login, name='login'),
    path('logout', agthi.views.logout, name='logout'),
    path('admin_home', agthi.views.admin_home, name='admin_home'),
    path('careers_adm', agthi.views.careers_adm, name='careers_adm'),
    path('view_vacancy_adm', agthi.views.view_vacancy_adm, name='view_vacancy_adm'),
    path('delete_vacancy_adm/<id>', agthi.views.delete_vacancy_adm, name='delete_vacancy_adm'),
    path('search_job', agthi.views.search_job, name='search_job'),
    path('edit_vacancy_adm/<id>', agthi.views.edit_vacancy_adm, name='edit_vacancy_adm'),
    path('apply_job/<id>', agthi.views.apply_job, name='apply_job'),
    path('view_job_apls', agthi.views.view_job_apls, name='view_job_apls'),
    path('search_job_apls', agthi.views.search_job_apls, name='search_job_apls'),
    path('delete_apln_adm/<id>', agthi.views.delete_apln_adm, name='delete_apln_adm'),
    path('media_page', agthi.views.media_page, name='media_page'),
    path('mnge_restaurants_adm', agthi.views.mnge_restaurants_adm, name='mnge_restaurants_adm'),
    path('images_restau_adm/<id>', agthi.views.images_restau_adm, name='images_restau_adm'),
    path('descr_restau_adm/<id>', agthi.views.descr_restau_adm, name='descr_restau_adm'),
    path('edit_img_resta_adm/<id>', agthi.views.edit_img_resta_adm, name='edit_img_resta_adm'),
    path('delete_img_resta_adm/<id>', agthi.views.delete_img_resta_adm, name='delete_img_resta_adm'),
    path('add_img_resta_adm', agthi.views.add_img_resta_adm, name='add_img_resta_adm'),
    path('edit_resta_adm/<id>', agthi.views.edit_resta_adm, name='edit_resta_adm'),
    path('delete_resta_adm/<id>', agthi.views.delete_resta_adm, name='delete_resta_adm'),
    path('add_resta_adm', agthi.views.add_resta_adm, name='add_resta_adm'),
    path('search_resta', agthi.views.search_resta, name='search_resta'),
    path('cust_subscr', agthi.views.cust_subscr, name='cust_subscr'),
    path('view_subscr_adm', agthi.views.view_subscr_adm, name='view_subscr_adm'),
    path('search_subscr', agthi.views.search_subscr, name='search_subscr'),
    path('delete_subscr_adm/<id>', agthi.views.delete_subscr_adm, name='delete_subscr_adm'),
    path('about_adm', agthi.views.about_adm, name='about_adm'),
    path('add_about_adm', agthi.views.add_about_adm, name='add_about_adm'),
    path('edit_about_adm/<id>', agthi.views.edit_about_adm, name='edit_about_adm'),
    path('delete_about_adm/<id>', agthi.views.delete_about_adm, name='delete_about_adm'),
    path('our_ple_adm', agthi.views.our_ple_adm, name='our_ple_adm'),
    path('edit_our_ple_adm/<id>', agthi.views.edit_our_ple_adm, name='edit_our_ple_adm'),
    path('delete_our_ple_adm/<id>', agthi.views.delete_our_ple_adm, name='delete_our_ple_adm'),
    path('add_our_ple_adm', agthi.views.add_our_ple_adm, name='add_our_ple_adm'),
    path('mission_adm', agthi.views.mission_adm, name='mission_adm'),
    path('edit_mission_adm/<id>', agthi.views.edit_mission_adm, name='edit_mission_adm'),
    path('delete_mission_adm/<id>', agthi.views.delete_mission_adm, name='delete_mission_adm'),
    path('add_mission_adm', agthi.views.add_mission_adm, name='add_mission_adm'),
    path('vision_adm', agthi.views.vision_adm, name='vision_adm'),
    path('edit_vision_adm/<id>', agthi.views.edit_vision_adm, name='edit_vision_adm'),
    path('delete_vision_adm/<id>', agthi.views.delete_vision_adm, name='delete_vision_adm'),
    path('add_vision_adm', agthi.views.add_vision_adm, name='add_vision_adm'),
    path('word_ceo_adm', agthi.views.word_ceo_adm, name='word_ceo_adm'),
    path('edit_word_ceo_adm/<id>', agthi.views.edit_word_ceo_adm, name='edit_word_ceo_adm'),
    path('delete_word_ceo_adm/<id>', agthi.views.delete_word_ceo_adm, name='delete_word_ceo_adm'),
    path('add_word_ceo_adm', agthi.views.add_word_ceo_adm, name='add_word_ceo_adm'),
    path('news_adm', agthi.views.news_adm, name='news_adm'),
    path('edit_media_adm/<id>', agthi.views.edit_media_adm, name='edit_media_adm'),
    path('delete_media_adm/<id>', agthi.views.delete_media_adm, name='delete_media_adm'),
    path('add_media_adm', agthi.views.add_media_adm, name='add_media_adm'),
    path('reser_unavailable', agthi.views.reser_unavailable, name='reser_unavailable'),
    path('link_unavailable', agthi.views.link_unavailable, name='link_unavailable'),
    path('link_unavailable1', agthi.views.link_unavailable1, name='link_unavailable1'),
    path('contact_us_adm', agthi.views.contact_us_adm, name='contact_us_adm'),
    path('add_contact_adm', agthi.views.add_contact_adm, name='add_contact_adm'),
    path('edit_contact_adm/<id>', agthi.views.edit_contact_adm, name='edit_contact_adm'),
    path('delete_contact_adm/<id>', agthi.views.delete_contact_adm, name='delete_contact_adm'),
]