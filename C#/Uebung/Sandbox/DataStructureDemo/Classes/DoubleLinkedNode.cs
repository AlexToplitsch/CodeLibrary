using System;
using System.Collections.Generic;
using System.Text;

namespace DataStructureDemo.Classes
{
    class DoubleLinkedNode
    {
        public string Value { get; set; }
        public DoubleLinkedNode Next { get; set; }
        public DoubleLinkedNode Prev { get; set; }
        public DoubleLinkedNode(string i = "")
        {
            Value = i;
        }
    }
}
