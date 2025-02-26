<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trắc nghiệm vai trò</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
        }
        h1 {
            text-align: center;
        }
        .question {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        select {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            display: block;
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
        }
        .result {
            margin-top: 20px;
            font-weight: bold;
            text-align: center;
        }
    </style>
</head>
<body>

    <h1>Trắc nghiệm vai trò của bạn</h1>

    <div class="question">
        <label>Câu 1: bạn là</label>
        <select id="question1">
            <option value="a">A: nam</option>
            <option value="b">B: nữ</option>
        </select>
    </div>

    <div class="question">
        <label>Câu 2: chiều cao và trọng lượng của bạn</label>
        <select id="question2">
            <option value="a">A: Bạn khá nhẹ</option>
            <option value="b">B: Bạn có thân hình trung bình và khỏe khắn</option>
            <option value="c">C: Bạn có thân hình tương đối cao lớn</option>
        </select>
    </div>

    <div class="question">
        <label>Câu 3: Bạn thích làm tâm điểm của sân khấu?</label>
        <select id="question3">
            <option value="a">A: Mình thích được tỏa sáng và thoải mái với việc đó</option>
            <option value="b">B: Mình thoải mái nhưng không cần thiết phải là tâm điểm</option>
            <option value="c">C: Mình thích đóng vai trò hỗ trợ hơn</option>
        </select>
    </div>

    <div class="question">
        <label>Câu 4: Điểm mạnh về thể chất của bạn</label>
        <select id="question4">
            <option value="a">A: Mình rất dẻo dai và có thể nhào lộn</option>
            <option value="b">B: Mình khỏe và nâng đỡ tốt</option>
            <option value="c">C: Mình có phản xạ tốt và linh hoạt</option>
        </select>
    </div>

    <button onclick="determineRole()">Xác định vai trò của bạn</button>

    <div class="result" id="result"></div>

    <script>
        function determineRole() {
            var q1 = document.getElementById('question1').value;
            var q2 = document.getElementById('question2').value;
            var q3 = document.getElementById('question3').value;
            var q4 = document.getElementById('question4').value;

            var result = '';

            if (q1 === 'a') {
                if ((q2 === 'b' || q2 === 'c') && (q3 === 'a' || q3 === 'b') && (q4 === 'a' || q4 === 'b')) {
                    result = 'Bạn là BASE';
                } else {
                    result = 'Bạn là BACK';
                }
            } else if (q1 === 'b') {
                if ((q2 === 'a' || q2 === 'b') && (q3 === 'a' || q3 === 'b') && (q4 === 'a' || q4 === 'c')) {
                    result = 'Bạn là FLYER';
                } else if (q2 === 'c' && q3 === 'a' && q4 === 'a') {
                    result = 'Bạn là FLYER';
                } else {
                    result = 'Bạn là BACK';
                }
            }

            document.getElementById('result').innerText = result;
        }
    </script>

</body>
</html>
</html>