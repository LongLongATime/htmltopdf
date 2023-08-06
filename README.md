# htmltopdf

htmltopdf是一个可以把网上文章批量导出成pdf的工具,相比现有的一些导出工具，有的要么不支持批量，有的要么需要收费。
<p>htmltopdf不是一个完善的工具产品，但提供了一种批量导出pdf的思路,大家可以借鉴和学习。</p>

常用的html导出成pdf的方法，一般有下面几种：
<p>1、wkhtmltopdf<p>
<p>原理是使用webKit引擎渲染出页面，然后再导出成pdf。</p>
<p>优点是成熟，被用于许多导出工具的底层库，如pdfkit</p>
<p>缺点是容易出现页面乱版。如页面有一个资源无法访问，可能导致导出的pdf排版乱序</p>

<p>2、pdfkit</p>
python编写，底层也是用了wkhtmltopdf。
<p>优点是易使用</p>
<p>缺点是容易像底层也是用了wkhtmltopdf一样容易出现页面乱版</p>

<p>3、selenium</p>
这是比较推荐的方案，因为直接只有浏览器的打印功能，导出和看到的页面一致，体验最好。

<p>4、借助一些平台</p>
<u>
<li>https://pdfmyurl.com/：不支持批量</li>
<li>其它支持批量的平台需要收费</li>
</u>

