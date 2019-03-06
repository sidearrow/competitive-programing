using System;
using System.Collections.Generic;

class Index
{
    static void Main()
    {
        string currentDir = System.IO.Directory.GetCurrentDirectory();
        // string inputFilePath = System.IO.Path.Combine(currentDir, "test.xlsx");
    
        Input input = new Input();
        Output output = new Output(input);
    }
}

public class Output
{
    public Output(Input input)
    {
        string res = "";
        foreach (Table table in input.tableList) {
            foreach (Field field in table.fieldList) {
                res += "$table->";
                res += this.getMethodName(field.type);
                res += "('";
                res += field.fieldName;
                res += "`);";
            }
        }
        Console.WriteLine(res);
    }

    private string getMethodName(FieldType fieldType)
    {
        if (fieldType == FieldType.NUMBER) {
            return "integer";
        }
        if (fieldType == FieldType.VARCHAR2) {
            return "string";
        }
        if (fieldType == FieldType.DATE) {
            return "time";
        }
        return "";
    }
}

public class Input
{
    public List<Table> tableList = new List<Table>();

    public Input()
    {
        List<string[]> inputTable = new List<string[]>();
        inputTable.Add(new string[] {"ID", "NUMBER", ""});
        inputTable.Add(new string[] {"NAME", "VARCHAR2", "10"});

        Table table = new Table();
        table.tableName = "table name";
        foreach (string[] _field in inputTable) {
            Field field = new Field();
            field.fieldName = _field[0];
            field.type      = this.getFieldType(_field[1]);
            field.length    = _field[2];
            table.fieldList.Add(field);
        }

        this.tableList.Add(table);
    }

    private FieldType getFieldType(string fieldTypeString)
    {
        if (fieldTypeString == "NUMBER") {
            return FieldType.NUMBER;
        }
        if (fieldTypeString == "VARCHAR2") {
            return FieldType.VARCHAR2;
        }
        if (fieldTypeString == "DATE") {
            return FieldType.DATE;
        }
        return FieldType.NUMBER;
    }
}

public class Table
{
    public string tableName;
    public List<Field> fieldList = new List<Field>();
}

public class Field
{
    public string fieldName;
    public FieldType type;
    public string length;
    public bool isDecimal = false;
    public bool isPrimaryKey = false;
    public bool isNotNull = false;
}

public enum FieldType
{
    NUMBER,
    VARCHAR2,
    DATE,
}