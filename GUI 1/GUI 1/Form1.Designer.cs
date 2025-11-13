namespace GUI_1
{
    partial class mainFrm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.tbNum1 = new System.Windows.Forms.TextBox();
            this.tbResult = new System.Windows.Forms.TextBox();
            this.tbNum2 = new System.Windows.Forms.TextBox();
            this.btAdd = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.tbMul = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.lbError = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.rb_Add = new System.Windows.Forms.RadioButton();
            this.rb_Sub = new System.Windows.Forms.RadioButton();
            this.rb_Mul = new System.Windows.Forms.RadioButton();
            this.rb_Div = new System.Windows.Forms.RadioButton();
            this.bt_Execute = new System.Windows.Forms.Button();
            this.bt_Clear = new System.Windows.Forms.Button();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(37, 37);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(62, 16);
            this.label1.TabIndex = 0;
            this.label1.Text = "number 1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(37, 72);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(62, 16);
            this.label2.TabIndex = 1;
            this.label2.Text = "number 2";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(54, 106);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(45, 16);
            this.label3.TabIndex = 2;
            this.label3.Text = "Result";
            // 
            // tbNum1
            // 
            this.tbNum1.Location = new System.Drawing.Point(114, 34);
            this.tbNum1.Name = "tbNum1";
            this.tbNum1.Size = new System.Drawing.Size(99, 22);
            this.tbNum1.TabIndex = 3;
            // 
            // tbResult
            // 
            this.tbResult.Location = new System.Drawing.Point(114, 103);
            this.tbResult.Name = "tbResult";
            this.tbResult.Size = new System.Drawing.Size(99, 22);
            this.tbResult.TabIndex = 4;
            // 
            // tbNum2
            // 
            this.tbNum2.Location = new System.Drawing.Point(114, 69);
            this.tbNum2.Name = "tbNum2";
            this.tbNum2.Size = new System.Drawing.Size(99, 22);
            this.tbNum2.TabIndex = 5;
            // 
            // btAdd
            // 
            this.btAdd.Location = new System.Drawing.Point(220, 37);
            this.btAdd.Name = "btAdd";
            this.btAdd.Size = new System.Drawing.Size(74, 40);
            this.btAdd.TabIndex = 6;
            this.btAdd.Text = "Add";
            this.btAdd.UseVisualStyleBackColor = true;
            this.btAdd.Click += new System.EventHandler(this.Add_Click);
            this.btAdd.MouseHover += new System.EventHandler(this.black);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(219, 83);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 39);
            this.button2.TabIndex = 7;
            this.button2.Text = "Sub";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.Sub_Click);
            // 
            // tbMul
            // 
            this.tbMul.Location = new System.Drawing.Point(320, 36);
            this.tbMul.Name = "tbMul";
            this.tbMul.Size = new System.Drawing.Size(75, 41);
            this.tbMul.TabIndex = 8;
            this.tbMul.Text = "Mul";
            this.tbMul.UseVisualStyleBackColor = true;
            this.tbMul.Click += new System.EventHandler(this.Mul_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(320, 83);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 39);
            this.button4.TabIndex = 9;
            this.button4.Text = "Div";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.Div_Click);
            // 
            // lbError
            // 
            this.lbError.AutoSize = true;
            this.lbError.Location = new System.Drawing.Point(185, 128);
            this.lbError.Name = "lbError";
            this.lbError.Size = new System.Drawing.Size(0, 16);
            this.lbError.TabIndex = 10;
            // 
            // groupBox1
            // 
            this.groupBox1.Location = new System.Drawing.Point(30, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(384, 132);
            this.groupBox1.TabIndex = 11;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Simple caculator";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.bt_Clear);
            this.groupBox2.Controls.Add(this.bt_Execute);
            this.groupBox2.Controls.Add(this.rb_Div);
            this.groupBox2.Controls.Add(this.rb_Mul);
            this.groupBox2.Controls.Add(this.rb_Sub);
            this.groupBox2.Controls.Add(this.rb_Add);
            this.groupBox2.Location = new System.Drawing.Point(434, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(228, 132);
            this.groupBox2.TabIndex = 12;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Operations";
            // 
            // rb_Add
            // 
            this.rb_Add.AutoSize = true;
            this.rb_Add.Location = new System.Drawing.Point(6, 22);
            this.rb_Add.Name = "rb_Add";
            this.rb_Add.Size = new System.Drawing.Size(53, 20);
            this.rb_Add.TabIndex = 0;
            this.rb_Add.TabStop = true;
            this.rb_Add.Text = "Add";
            this.rb_Add.UseVisualStyleBackColor = true;
            // 
            // rb_Sub
            // 
            this.rb_Sub.AutoSize = true;
            this.rb_Sub.Location = new System.Drawing.Point(6, 48);
            this.rb_Sub.Name = "rb_Sub";
            this.rb_Sub.Size = new System.Drawing.Size(52, 20);
            this.rb_Sub.TabIndex = 1;
            this.rb_Sub.TabStop = true;
            this.rb_Sub.Text = "Sub";
            this.rb_Sub.UseVisualStyleBackColor = true;
            // 
            // rb_Mul
            // 
            this.rb_Mul.AutoSize = true;
            this.rb_Mul.Location = new System.Drawing.Point(6, 74);
            this.rb_Mul.Name = "rb_Mul";
            this.rb_Mul.Size = new System.Drawing.Size(49, 20);
            this.rb_Mul.TabIndex = 2;
            this.rb_Mul.TabStop = true;
            this.rb_Mul.Text = "Mul";
            this.rb_Mul.UseVisualStyleBackColor = true;
            // 
            // rb_Div
            // 
            this.rb_Div.AutoSize = true;
            this.rb_Div.Location = new System.Drawing.Point(6, 100);
            this.rb_Div.Name = "rb_Div";
            this.rb_Div.Size = new System.Drawing.Size(48, 20);
            this.rb_Div.TabIndex = 3;
            this.rb_Div.TabStop = true;
            this.rb_Div.Text = "Div";
            this.rb_Div.UseVisualStyleBackColor = true;
            // 
            // bt_Execute
            // 
            this.bt_Execute.Location = new System.Drawing.Point(125, 15);
            this.bt_Execute.Name = "bt_Execute";
            this.bt_Execute.Size = new System.Drawing.Size(85, 50);
            this.bt_Execute.TabIndex = 4;
            this.bt_Execute.Text = "Execute";
            this.bt_Execute.UseVisualStyleBackColor = true;
            this.bt_Execute.Click += new System.EventHandler(this.bt_Execute_Click);
            // 
            // bt_Clear
            // 
            this.bt_Clear.Location = new System.Drawing.Point(125, 71);
            this.bt_Clear.Name = "bt_Clear";
            this.bt_Clear.Size = new System.Drawing.Size(85, 46);
            this.bt_Clear.TabIndex = 5;
            this.bt_Clear.Text = "Clear";
            this.bt_Clear.UseVisualStyleBackColor = true;
            this.bt_Clear.Click += new System.EventHandler(this.bt_Clear_Click);
            // 
            // mainFrm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(710, 176);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.lbError);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.tbMul);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.btAdd);
            this.Controls.Add(this.tbNum2);
            this.Controls.Add(this.tbResult);
            this.Controls.Add(this.tbNum1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.groupBox1);
            this.Name = "mainFrm";
            this.Text = "Hello GUI";
            this.Load += new System.EventHandler(this.mainFrm_Load);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tbNum1;
        private System.Windows.Forms.TextBox tbResult;
        private System.Windows.Forms.TextBox tbNum2;
        private System.Windows.Forms.Button btAdd;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button tbMul;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Label lbError;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.RadioButton rb_Div;
        private System.Windows.Forms.RadioButton rb_Mul;
        private System.Windows.Forms.RadioButton rb_Sub;
        private System.Windows.Forms.RadioButton rb_Add;
        private System.Windows.Forms.Button bt_Clear;
        private System.Windows.Forms.Button bt_Execute;
    }
}

