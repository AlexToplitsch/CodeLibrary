using System;
using System.Collections.Generic;
using System.Text;

namespace DataStructureDemo.Classes
{
    public class SingleLinkedNode
    {
        public int Value { get; set; }
        public SingleLinkedNode Next { get; set; }
        public SingleLinkedNode(int v, SingleLinkedNode n = null)
        {
            Value = v;
            Next = n;
        }

        public void DisplayNode()
        {
            if(Next == null)
            {
                Console.WriteLine($"Value = {Value} Next = Null");
                return;
            }
            Console.WriteLine($"Value = {Value} Next = {Next.GetType()}");
        }
    }
}
