import{B as _}from"./Base.ebed360e.js";import{D as p}from"./DeckForm.6cd1445a.js";import{D as f}from"./DynamicContent.17061b9b.js";import{_ as u,A as o}from"./index.5636f22e.js";import{r as c,o as a,d as D,w as r,f as g,h as d,t as n,j as x,F as B,k as C,g as i}from"./vendor.9a0731a0.js";const F={components:{Base:_,DeckForm:p,DynamicContent:f},data(){return{loaded:!1,deck:{},cards:[],deckId:this.$route.params.deck_id}},created(){this.$store.commit("setTitle","Edit Deck"),this.fetchData()},methods:{fetchData(){o.get(`decks/${this.deckId}`).then(t=>{this.loaded=!0,this.deck=t.deck,this.cards=t.cards}).catch(()=>{})},deckSubmit(t){o.put(`decks/${this.deckId}`,new FormData(t)).then(()=>{this.fetchData()}).catch(()=>{})}}},S={class:"mb-4"};function b(t,y,w,I,e,m){const k=c("DeckForm"),h=c("DynamicContent"),l=c("Base");return a(),D(l,null,{default:r(()=>{var s;return[g("h2",S,[d(n((s=e.deck.name)!=null?s:"Edit Deck")+" ",1),e.cards.length>0?(a(),x(B,{key:0},[d("("+n(e.cards.length)+" cards)",1)],64)):C("",!0)]),i(h,{loaded:e.loaded},{default:r(()=>[i(k,{existingDeck:e.deck,existingCards:e.cards,deckSubmit:m.deckSubmit},null,8,["existingDeck","existingCards","deckSubmit"])]),_:1},8,["loaded"])]}),_:1})}var T=u(F,[["render",b]]);export{T as default};
