import{B as r}from"./Base.ebed360e.js";import{D as m}from"./DeckForm.6cd1445a.js";import{_ as n,A as d}from"./index.5636f22e.js";import{r as o,o as i,d as p,w as _,g as k,f as u,t as l}from"./vendor.9a0731a0.js";const f={components:{Base:r,DeckForm:m},created(){this.$store.commit("setTitle","Create Deck")},methods:{deckSubmit(e){d.put("decks",new FormData(e)).then(t=>{this.$router.push({name:"decks.show",params:{deck_id:t.deck.id}})}).catch(()=>{})}}},h=u("h2",{class:"mb-4"},l("Add new deck"),-1);function B(e,t,D,b,w,s){const a=o("DeckForm"),c=o("Base");return i(),p(c,null,{default:_(()=>[h,k(a,{deckSubmit:s.deckSubmit},null,8,["deckSubmit"])]),_:1})}var F=n(f,[["render",B]]);export{F as default};
