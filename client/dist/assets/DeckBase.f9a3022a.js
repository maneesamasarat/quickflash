import{D as d,f as l}from"./date.8518464d.js";import{_}from"./index.5636f22e.js";import{r as i,o,j as m,f as s,h as c,t,d as k,k as v,l as f}from"./vendor.9a0731a0.js";const h={props:["deck"],components:{DeckIcon:d},methods:{fromNow:l}},w={class:"card"},u={class:"card-body pb-4"},D={class:"d-flex align-items-center"},b={class:"mb-4"},N=s("br",null,null,-1),p=c("Last score: ");function B(a,x,e,g,y,r){const n=i("DeckIcon");return o(),m("div",w,[s("div",u,[s("h4",D,[c(t(e.deck.name)+" ",1),e.deck.last_review?(o(),k(n,{key:0,score:e.deck.last_review.score_percent},null,8,["score"])):v("",!0)]),s("p",b,[c(t(e.deck.last_review?"Last reviewed "+r.fromNow(e.deck.last_review.taken_at)+" ago":"Never reviewed")+" ",1),N,p,s("b",null,t(e.deck.last_review?e.deck.last_review.score_percent+"%":"Unavailable"),1)]),f(a.$slots,"default")])])}var L=_(h,[["render",B]]);export{L as D};
