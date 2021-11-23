namespace WindowsFormsApp1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Btn_Right = new System.Windows.Forms.Button();
            this.Btn_Fight = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.Btn_Down = new System.Windows.Forms.Button();
            this.Btn_Up = new System.Windows.Forms.Button();
            this.Btn_Left = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // Btn_Right
            // 
            this.Btn_Right.Location = new System.Drawing.Point(816, 601);
            this.Btn_Right.Name = "Btn_Right";
            this.Btn_Right.Size = new System.Drawing.Size(30, 30);
            this.Btn_Right.TabIndex = 2;
            this.Btn_Right.Text = "►";
            this.Btn_Right.UseVisualStyleBackColor = true;
            this.Btn_Right.Click += new System.EventHandler(this.Btn_Right_Click);
            // 
            // Btn_Fight
            // 
            this.Btn_Fight.Location = new System.Drawing.Point(752, 677);
            this.Btn_Fight.Name = "Btn_Fight";
            this.Btn_Fight.Size = new System.Drawing.Size(94, 29);
            this.Btn_Fight.TabIndex = 2;
            this.Btn_Fight.Text = "Fight";
            this.Btn_Fight.UseVisualStyleBackColor = true;
            this.Btn_Fight.Click += new System.EventHandler(this.Btn_Fight_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(13, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(833, 279);
            this.pictureBox1.TabIndex = 3;
            this.pictureBox1.TabStop = false;
            // 
            // Btn_Down
            // 
            this.Btn_Down.Location = new System.Drawing.Point(788, 637);
            this.Btn_Down.Name = "Btn_Down";
            this.Btn_Down.Size = new System.Drawing.Size(30, 30);
            this.Btn_Down.TabIndex = 2;
            this.Btn_Down.Text = "▼";
            this.Btn_Down.UseVisualStyleBackColor = true;
            this.Btn_Down.Click += new System.EventHandler(this.Btn_Down_Click);
            // 
            // Btn_Up
            // 
            this.Btn_Up.Location = new System.Drawing.Point(788, 565);
            this.Btn_Up.Name = "Btn_Up";
            this.Btn_Up.Size = new System.Drawing.Size(30, 30);
            this.Btn_Up.TabIndex = 2;
            this.Btn_Up.Text = "▲";
            this.Btn_Up.UseVisualStyleBackColor = true;
            this.Btn_Up.Click += new System.EventHandler(this.Btn_Up_Click);
            // 
            // Btn_Left
            // 
            this.Btn_Left.Location = new System.Drawing.Point(759, 601);
            this.Btn_Left.Name = "Btn_Left";
            this.Btn_Left.Size = new System.Drawing.Size(30, 30);
            this.Btn_Left.TabIndex = 2;
            this.Btn_Left.Text = "◄";
            this.Btn_Left.UseVisualStyleBackColor = true;
            this.Btn_Left.Click += new System.EventHandler(this.Btn_Left_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 297);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(636, 409);
            this.richTextBox1.TabIndex = 4;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(858, 718);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.Btn_Left);
            this.Controls.Add(this.Btn_Up);
            this.Controls.Add(this.Btn_Down);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.Btn_Fight);
            this.Controls.Add(this.Btn_Right);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Button Btn_Right;
        private System.Windows.Forms.Button Btn_Fight;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button Btn_Down;
        private System.Windows.Forms.Button Btn_Up;
        private System.Windows.Forms.Button Btn_Left;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

