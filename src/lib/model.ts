export type Block={index:number;data:string;previousHash:string;hash:string};
export function hash(index:number,data:string,previousHash:string){let n=2166136261;for(const c of JSON.stringify([index,data,previousHash])){n^=c.charCodeAt(0);n=Math.imul(n,16777619)}return (n>>>0).toString(16).padStart(8,'0')}
export function block(index:number,data:string,previousHash:string):Block{return {index,data,previousHash,hash:hash(index,data,previousHash)}}
export function initialChain(){const a=block(0,'Бронь #A102','00000000');const b=block(1,'Оплата подтверждена',a.hash);return [a,b,block(2,'Отель подтвердил номер',b.hash)]}
export function validity(chain:Block[]){let valid=true;return chain.map((b,i)=>{valid=valid&&b.index===i&&b.hash===hash(b.index,b.data,b.previousHash)&&b.previousHash===(i?chain[i-1].hash:'00000000');return valid})}
export function contract(delay:number,verified:boolean){return !verified?'Нет подтверждения от оракула':delay>=120?'Условие выполнено → выплата предусмотрена':'Порог 120 минут не достигнут'}
export const defaults=[10000,15,300,0];
export function clean(n:number,max=1000000){return Number.isFinite(n)?Math.min(max,Math.max(0,n)):0}
export function costs(values:number[]){const [base,percent,fee,extra]=values;const platform=clean(base)*(1+clean(percent,100)/100);const protocol=clean(base)+clean(fee)+clean(extra);return {platform,protocol,difference:platform-protocol}}
