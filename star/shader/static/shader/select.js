var selectHead = document.getElementsByClassName('select-head')[0];
var selectHeadCont = document.getElementsByClassName('select-head-cont');
var Option = document.getElementsByClassName('option')[0];
var optionItem = document.getElementsByClassName('option-item');

/*默认是第一个选项*/
selectHeadCont[0].innerHTML = optionItem[0].innerHTML;

/*点击后出现下拉框*/
selectHead.addEventListener('click',function()
{
    Option.style.display = 'block';
},false);

/*点击选项后出现在下拉框*/
var len = optionItem.length;
for(var i=0;i<len;i++){
    optionItem[i].index = i;
    optionItem[i].addEventListener('click',function(){
        selectHeadCont[0].innerHTML = optionItem[this.index].innerHTML;
        Option.style.display = 'none';
    },false);
}
/*点击其他地方时，select会收起来*/
document.body.addEventListener('click',function(){
    Option.style.display = 'none';
}.false);

