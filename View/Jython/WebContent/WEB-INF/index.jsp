<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html lang="kor">
<head>
    <meta charset="UTF-8">
    <title>Test app</title>
    <link href="style/index.css" type="text/css" rel="stylesheet">
    <script src="style/index.js"></script>
</head>
<body>
<!--ù ȭ��.-->
<header>
    Recommend movie test
    <button class="circle" onclick="first()">First?</button>
</header>
<nav>
</nav>
<article>
    <div class="chat-window">
        <div class="conversation-view">
            <div class="chat-bubble me"><span class="chat-content">�α� �ִ� ��ȭ</span></div>
            <div class="chat-bubble"><span class="chat-content">���� �α� �ִ� ��ȭ�Դϴ�.</span></div>
            <div class="chat-bubble">
                <span class="chat-content">
                    <div class="movie">
                        <img src="img/2YAu2ctaxVGisdbmbbG35LXpQNp.jpg"><br>
                        Fast Color
                    </div>
                    <div class="movie">
                        <img src="img/2oa5oLm4FfjxvasKAW07wTrQ7Ow.jpg"><br>
                        Memories of My Body
                    </div>
                    <div class="movie">
                        <img src="img/o6oaiuJpfLDaGgu5TDW10dPxL0x.jpg"><br>
                        Murder Me, Monster
                    </div>
                </span>
            </div>
            <div class="chat-bubble"><span class="chat-content">�� �˾ƺ��ðڽ��ϱ�?</span></div>
            <div class="chat-bubble me"><span class="chat-content">�� ������</span></div>
            <div class="chat-bubble">
                <span class="chat-content">
                    <div class="movie">
                        <img src="img/g1tSdTXWv0iKDAXbrIfnFa7vgl4.jpg"><br>
                        Love on a Leash
                    </div>
                    <div class="movie">
                        <img src="img/WK9ehj4nEMvJNmFaWgll54v9yL.jpg"><br>
                        So, What's Your Price?
                    </div>
                    <div class="movie">
                        <img src="img/6EOV65KBIpn7SNUZouLlGZmPXCo.jpg"><br>
                        Endless
                    </div>
                </span>
            </div>
        </div>
        <div class="message-box">
            <form name="form" onsubmit="return false;">
                <input onkeyup="enterkey();" name="quest" class="text-input" type="text" autofocus placeholder="� ��ȭ�� ��� ������!" />
                <input type="button" class="text-submit" value="����" onclick="Quest()">
            </form>
        </div>
    </div>
</article>
<footer>
</footer>
<script src="style/index.js"></script>
</body>
</html>