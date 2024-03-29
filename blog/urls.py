from django.urls import path
from blog.views import (
    home,
    companyPlantedTree,
    treeList,
    faqList,
    plantedTree,
    register,
    donate,
    donateProject,
    toshkentVil,
    treeDetail,
    andijon,
    buxoro,
    namangan,
    navoiy,
    qashqadaryo,
    qoraqolpoq,
    samarqand,
    sirdaryo,
    surxondaryo,
    xorazm,
    fargona,
    respublika,
    jizzax,
    toshshahar,
    payment,
    clickPayment
)


urlpatterns = [
    path("", home, name="home"),
    path('tree-list', treeList, name="tree-list"),
    path('tree-detail/<int:id>', treeDetail, name="tree-detail"),
    path('company-planted-tree', companyPlantedTree, name="company-planted"),
    path('faq-list', faqList, name="faq-list"),
    path('planted-tree', plantedTree, name="planted-trees"),
    path('register', register, name='register'),
    path('donate', donate, name="donate"),
    path('donate-projects', donateProject, name="donate-projects"),
    path('toshkentVil', toshkentVil, name="toshkentVil"),
    path('andijon', andijon, name="andijon"),
    path('buxoro', buxoro, name="buxoro"),
    path('namangan', namangan, name="namangan"),
    path('navoiy', navoiy, name="navoiy"),
    path('qashqadaryo', qashqadaryo, name="qashqadaryo"),
    path('qoraqolpoq', qoraqolpoq, name="qoraqolpoq"),
    path('samarqand', samarqand, name="samarqand"),
    path('sirdaryo', sirdaryo, name="sirdaryo"),
    path('surxondaryo', surxondaryo, name="surxondaryo"),
    path('xorazm', xorazm, name="xorazm"),
    path('fargona', fargona, name="fargona"),
    path('respublika', respublika, name="respublika"),
    path('jizzax', jizzax, name="jizzax"),
    path('toshshahar', toshshahar, name="toshshahar"),
    path('payment', payment, name="payment"),
    path('clickPayment', clickPayment, name="clickPayment")
    ]